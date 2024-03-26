'''
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning


BaseException: The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined exceptions.
BaseExceptionGroup: A special group class that contains all built-in exceptions.
GeneratorExit: Raised when a generator's close() method is called.
KeyboardInterrupt: Raised when the user interrupts the execution of the program, typically by pressing Ctrl+C.
SystemExit: Raised by the sys.exit() function to exit the program.
Exception: The base class for all non-exit exceptions.
ArithmeticError: The base class for arithmetic errors.
FloatingPointError: Raised when a floating-point operation fails.
OverflowError: Raised when an arithmetic operation exceeds the limits of the current Python runtime environment.
ZeroDivisionError: Raised when the second operand of a division or modulo operation is zero.
AssertionError: Raised when an assert statement fails.
AttributeError: Raised when an attribute reference or assignment fails.
BufferError: Raised when a buffer-related operation cannot be performed.
EOFError: Raised when the input() function hits an end-of-file condition (EOF) without reading any data.
ExceptionGroup: A special group class that contains all non-exit exceptions.
ImportError: Raised when the imported module is not found.
ModuleNotFoundError: Raised when the imported module is not found.
LookupError: The base class for lookup errors.
IndexError: Raised when a sequence subscript is out of range.
KeyError: Raised when a dictionary key is not found in the set of existing keys.
MemoryError: Raised when an operation runs out of memory.
NameError: Raised when a local or global name is not found.
UnboundLocalError: Raised when a local variable is referenced before it has been assigned a value.
OSError: The base class for system-related errors.
BlockingIOError: Raised when an operation would block on an object set for non-blocking operation.
ChildProcessError: Raised when an error occurs in the child process during a subprocess operation.
ConnectionError: The base class for connection-related errors.
BrokenPipeError: Raised when trying to write to a pipe while the other end has been closed.
ConnectionAbortedError: Raised when a connection attempt is aborted by the network.
ConnectionRefusedError: Raised when a connection attempt is refused by the peer.
ConnectionResetError: Raised when the connection is reset by the peer.
FileExistsError: Raised when trying to create a file or directory that already exists.
FileNotFoundError: Raised when a file or directory is requested but cannot be found.
InterruptedError: Raised when a system call is interrupted by an incoming signal.
IsADirectoryError: Raised when a file operation (such as os.remove()) is requested on a directory.
NotADirectoryError: Raised when a directory operation (such as os.listdir()) is requested on a file.
PermissionError: Raised when trying to perform an operation without the adequate permissions.
ProcessLookupError: Raised when a given process does not exist.
TimeoutError: Raised when a timeout occurs during a socket operation.
ReferenceError: Raised when a weak reference proxy is used to access a garbage-collected referent.
RuntimeError: The base class for runtime errors.
NotImplementedError: Raised when an abstract method that should be implemented in a subclass is not actually implemented.
RecursionError: Raised when the maximum recursion depth is exceeded.
StopAsyncIteration: Raised by an async iterator's anext() method to signal the end of iteration.
StopIteration: Raised by the next() function to indicate that there are no further items to be returned by an iterator.
SyntaxError: Raised when there is a syntax error in the code.
IndentationError: Raised when indentation is not properly aligned.
TabError: Raised when the indentation consists of inconsistent tabs and spaces in the source code.
SystemError: Raised when the interpreter encounters an internal error, which usually indicates a bug in the interpreter itself.
TypeError: Raised when an operation or function is applied to an object of an inappropriate type.
ValueError: Raised when a built-in operation or function receives an argument with the right type but an inappropriate value.
UnicodeError: The base class for Unicode-related errors.
UnicodeDecodeError: Raised when decoding Unicode fails.
UnicodeEncodeError: Raised when encoding Unicode fails.
UnicodeTranslateError: Raised when translating Unicode fails.
Warning: The base class for warning categories.
BytesWarning: Base category for bytes-related warnings.
DeprecationWarning: Base category for warnings about deprecated features.
EncodingWarning: Base category for warnings about encoding issues.
FutureWarning: Base category for warnings about constructs that will change semantically in the future.
ImportWarning: Base category for warnings about probable mistakes in imports.
PendingDeprecationWarning: Base category for warnings about features that will be deprecated in the future.
ResourceWarning: Base category for warnings about resource usage issues.
RuntimeWarning: Base category for warnings about suspicious runtime behavior.
SyntaxWarning: Base category for warnings about dubious syntax.
UnicodeWarning: Base category for warnings about Unicode-related issues.
UserWarning: A warning category intended for user-defined warnings.           
'''

raise