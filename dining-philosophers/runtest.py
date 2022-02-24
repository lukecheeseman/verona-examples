import os
import time

# This will measure setup and teardown time

if __name__ == "__main__":
    for acquire in ["all", "one"]:
        for num in range(1, os.cpu_count() + 1):
            print(f"acquiring {acquire} with {num} cpus", end="", flush=True)
            total = 0
            for exp in range(100):
                start = time.time()
                os.system(f"../../verona/build-acquire-{acquire}/dist/veronac throughput.verona --run-cores={num} --run")
                end = time.time()
                total += (end - start)
                if exp % 10 == 0:
                    print(".", end="", flush=True)
            print(f" took {total/100}s on average")

