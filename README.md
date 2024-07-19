# Bitcoin Puzzle Solver

## Overview

The Bitcoin Puzzle Solver is a Python script designed to solve the Bitcoin Challenge Puzzle by brute-forcing private keys to match a given Bitcoin address. It employs parallel processing to efficiently search through a range of private keys. The solver includes both a command-line interface (CLI) and a graphical user interface (GUI) for flexibility in usage.

## Features

- **Parallel Processing**: Uses multiple CPU cores to speed up the search process.
- **Dynamic Bitcoin Address**: Allows specifying the target Bitcoin address dynamically.
- **Command-Line Interface (CLI)**: Configure parameters directly via command-line arguments.
- **Graphical User Interface (GUI)**: User-friendly interface for configuration and execution.
- **Detailed Logging**: Logs process details and errors for tracking.

## Requirements

- Python 3.x
- `bitcoin` library
- `tkinter` (for GUI)
- `concurrent.futures` (for parallel processing)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/amariwan/bitcoin-puzzle-solver.git
   cd bitcoin-puzzle-solver
   ```

2. **Install Dependencies**

   Install the required Python packages using `pip`. 

   ```bash
   pip install bitcoin
   ```

3. **Additional Setup**

   For GUI functionality, `tkinter` is usually included with Python installations. If not, it can be installed separately.

## Usage

### Command-Line Interface (CLI)

To run the solver using the command line, use the following command:

```bash
python main.py --min <MIN_KEY> --max <MAX_KEY> --wallet <TARGET_WALLET> --chunks <NUM_CHUNKS>
```

- `--min <MIN_KEY>`: Minimum value of the private key range (default: `0x8000`)
- `--max <MAX_KEY>`: Maximum value of the private key range (default: `0xffff`)
- `--wallet <TARGET_WALLET>`: Target Bitcoin address to match (required)
- `--chunks <NUM_CHUNKS>`: Number of chunks to divide the keyspace for parallel processing (default: number of CPU cores)

**Example CLI Command:**

```bash
python main.py --min 32768 --max 65535 --wallet 3tYXja42qDfN8B72mZCPWEu1oTn9LksPhB --chunks 4
```

### Graphical User Interface (GUI)

To run the GUI, execute:

```bash
python main_gui.py
```

In the GUI:
- Enter the minimum and maximum private key values.
- Provide the target Bitcoin address.
- Specify the number of chunks for parallel processing.
- Click "Start" to begin solving the puzzle.

**Example GUI Configuration:**

- Minimum Key: `32768`
- Maximum Key: `65535`
- Target Wallet: `3tYXja42qDfN8B72mZCPWEu1oTn9LksPhB`
- Chunks: `4`

Click "Start" to begin solving the puzzle.

## Logging

All output, including errors and results, will be logged to `bitcoin_puzzle.log`. This log file will help you track the solver's progress and diagnose any issues.

## Contributing

Contributions to the Bitcoin Puzzle Solver are welcome! If you have suggestions, improvements, or bug fixes, please submit a pull request or open an issue in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or further assistance, please reach out to:

- Email: [dev@tasiomind.de](mailto:dev@tasiomind.de)
- GitHub: [amariwan](https://github.com/amariwan)

