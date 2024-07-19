import bitcoin
import binascii
import time
import logging
import argparse
import concurrent.futures
from typing import Optional
from multiprocessing import cpu_count

# Configuration for Logging
logging.basicConfig(filename='bitcoin_puzzle.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BitcoinPuzzleSolver:
    def __init__(self, min_key: int, max_key: int, wallet: str, chunks: int):
        self.min_key = min_key
        self.max_key = max_key
        self.wallet = wallet
        self.chunks = chunks
        self.chunk_size = (max_key - min_key) // chunks
        self.address_cache = {}  # Caching results

    def generate_public(self, private_key_hex: str) -> Optional[str]:
        """ Generate Bitcoin address from a private key. """
        if private_key_hex in self.address_cache:
            return self.address_cache[private_key_hex]

        try:
            priv_key_bytes = binascii.unhexlify(private_key_hex)
            pub_key = bitcoin.privkey_to_pubkey(priv_key_bytes)
            public_address = bitcoin.pubkey_to_address(pub_key)
            self.address_cache[private_key_hex] = public_address
            return public_address
        except Exception as e:
            logging.error(f"Error generating public key for {private_key_hex}: {e}")
            return None

    def run_bf(self, start: int, end: int) -> Optional[str]:
        """ Brute-force search for the private key. """
        for key in range(start, end):
            pkey_hex = hex(key)[2:].zfill(64)  # Format to 64 hex digits
            public_address = self.generate_public(pkey_hex)

            if public_address == self.wallet:
                logging.info(f"Found! Private Key: {pkey_hex}")
                return pkey_hex

        return None

    def process_chunk(self, chunk_id: int, start: int, end: int) -> Optional[str]:
        """ Process a chunk of the keyspace. """
        logging.info(f"Processing chunk {chunk_id}: {start} - {end}")
        found_key = self.run_bf(start, end)
        if found_key:
            logging.info(f"Chunk {chunk_id} found key: {found_key}")
            return found_key
        logging.info(f"Chunk {chunk_id} completed without finding the key.")
        return None

    def solve(self) -> Optional[str]:
        """ Start solving the Bitcoin puzzle. """
        with concurrent.futures.ProcessPoolExecutor(max_workers=self.chunks) as executor:
            futures = []
            for i in range(self.chunks):
                start = self.min_key + i * self.chunk_size
                end = start + self.chunk_size if i < self.chunks - 1 else self.max_key
                futures.append(executor.submit(self.process_chunk, i, start, end))

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    return result
        return None

def parse_arguments() -> argparse.Namespace:
    """ Parse command line arguments. """
    parser = argparse.ArgumentParser(description='Solve Bitcoin Puzzle by Brute-Force.')
    parser.add_argument('--min', type=int, default=0x8000, help='Minimum value of the private key range')
    parser.add_argument('--max', type=int, default=0xffff, help='Maximum value of the private key range')
    parser.add_argument('--wallet', type=str, required=True, help='Target Bitcoin address to match')
    parser.add_argument('--chunks', type=int, default=cpu_count(), help='Number of chunks to divide the keyspace')
    return parser.parse_args()

def main():
    args = parse_arguments()
    start_time = time.time()
    solver = BitcoinPuzzleSolver(min_key=args.min, max_key=args.max, wallet=args.wallet, chunks=args.chunks)
    found_key = solver.solve()
    elapsed_time = time.time() - start_time
    if found_key:
        logging.info(f"Key found: {found_key}")
    else:
        logging.info("No key found within the given range.")
    logging.info(f"Total time: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
