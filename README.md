# Basic Python Project

## Python Project Initialisation

- `choco install python --version=3.10.0 --force` : some packages are not compatible with 3.11 or 3.12
- `python -m venv .venv`
- `source .venv/Scripts/activate` : to call on each terminal each time
- `python -m pip install --upgrade pip`
- `pip install -r requirements.txt`
- for indentation: `black .` to format code

## Explanation

workers = 4, on an 8-core CPU.

- We have 4 processes (workers)
- Each worker has a thread pool of ~12 threads min(32, cpu_count() + 4)

That means:

- CPU-bound (def + pure Python: While, for, ...): parallelism ≈ workers (processes): The GIL (Global Interpreter Lock) allows ~one running Python thread per process
- IO-bound (def: network: DB, File, ...): parallelism ≈ workers *threads (threads per process) = 4* 12 = 48 threads
- Async (async def): high concurrency via await, many requests can be served concurrently unless code is blocking
