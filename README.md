# 2019-talk-demo-async
Demo Code for "Introduction to Asynchronous Programming" (2019)

## Code Organization

Here are the main sections:

* A simple webserver to simulate an external resource that consumes a CPU resource in a controlled manner
* Demo 1: getting a number of (web) resources concurrently (use cases: how it works, code simplicity)
  * A for-loop approach
  * A low-level thread approach
  * A ThreadPoolExecutor approach
  * A async/await approach
* Demo 2: upgraded demo 1 with cancellable tasks (use case: thread/task cancellation)
  * May have to cite CPython code on how cancellation works.
  * May use a web service to trigger the job initiation and cancellation.
* Demo 3: thread-safe example in asyncio... This may not happen if the demo is difficult to set up.
