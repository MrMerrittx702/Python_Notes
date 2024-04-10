'Exceptions Try-Except'

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
       
'''



# raise BaseException# The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined exceptions.
# # BaseExceptionGroup A special group class that contains all built-in exceptions.
# raise GeneratorExit# Raised when a generator's close() method is called.
# raise KeyboardInterrupt# Raised when the user interrupts the execution of the program, typically by pressing Ctrl+C.
# raise SystemExit# Raised by the sys.exit() function to exit the program.
# raise Exception# The base class for all non-exit exceptions.
# raise ArithmeticError# The base class for arithmetic errors.
# raise FloatingPointError# Raised when a floating-point operation fails.
# raise OverflowError# Raised when an arithmetic operation exceeds the limits of the current Python runtime environment.
# raise ZeroDivisionError# Raised when the second operand of a division or modulo operation is zero.
# raise AssertionError# Raised when an assert statement fails.
# raise AttributeError# Raised when an attribute reference or assignment fails.
# raise BufferError# Raised when a buffer-related operation cannot be performed.
# raise EOFError# Raised when the input() function hits an end-of-file condition (EOF) without reading any data.
# # ExceptionGroup A special group class that contains all non-exit exceptions.raise 
# raise ImportError# Raised when the imported module is not found.
# raise ModuleNotFoundError# Raised when the imported module is not found.
# raise LookupError# The base class for lookup errors.
# raise IndexError# Raised when a sequence subscript is out of range.
# raise KeyError# Raised when a dictionary key is not found in the set of existing keys.
# raise MemoryError# Raised when an operation runs out of memory.
# raise NameError# Raised when a local or global name is not found.
# raise UnboundLocalError# Raised when a local variable is referenced before it has been assigned a value.
# raise OSError# The base class for system-related errors.
# raise BlockingIOError# Raised when an operation would block on an object set for non-blocking operation.
# raise ChildProcessError# Raised when an error occurs in the child process during a subprocess operation.
# raise ConnectionError# The base class for connection-related errors.
# raise BrokenPipeError# Raised when trying to write to a pipe while the other end has been closed.
# raise ConnectionAbortedError# Raised when a connection attempt is aborted by the network.
# raise ConnectionRefusedError# Raised when a connection attempt is refused by the peer.
# raise ConnectionResetError# Raised when the connection is reset by the peer.
# raise FileExistsError# Raised when trying to create a file or directory that already exists.
# raise FileNotFoundError# Raised when a file or directory is requested but cannot be found.
# raise InterruptedError# Raised when a system call is interrupted by an incoming signal.
# raise IsADirectoryError# Raised when a file operation (such as os.remove()) is requested on a directory.
# raise NotADirectoryError# Raised when a directory operation (such as os.listdir()) is requested on a file.
# raise PermissionError# Raised when trying to perform an operation without the adequate permissions.
# raise ProcessLookupError# Raised when a given process does not exist.
# raise TimeoutError# Raised when a timeout occurs during a socket operation.
# raise ReferenceError# Raised when a weak reference proxy is used to access a garbage-collected referent.
# raise RuntimeError# The base class for runtime errors.
# raise NotImplementedError# Raised when an abstract method that should be implemented in a subclass is not actually implemented.
# raise RecursionError# Raised when the maximum recursion depth is exceeded.
# raise StopAsyncIteration# Raised by an async iterator's anext() method to signal the end of iteration.
# raise StopIteration# Raised by the next() function to indicate that there are no further items to be returned by an iterator.
# raise SyntaxError# Raised when there is a syntax error in the code.
# raise IndentationError# Raised when indentation is not properly aligned.
# raise TabError# Raised when the indentation consists of inconsistent tabs and spaces in the source code.
# raise SystemError# Raised when the interpreter encounters an internal error, which usually indicates a bug in the interpreter itself.
# raise TypeError# Raised when an operation or function is applied to an object of an inappropriate type.
# raise ValueError# Raised when a built-in operation or function receives an argument with the right type but an inappropriate value.
# raise UnicodeError# The base class for Unicode-related errors.
# raise UnicodeDecodeError# Raised when decoding Unicode fails.
# raise UnicodeEncodeError# Raised when encoding Unicode fails.
# raise UnicodeTranslateError# Raised when translating Unicode fails.
# raise Warning# The base class for warning categories.
# raise BytesWarning# Base category for bytes-related warnings.
# raise DeprecationWarning# Base category for warnings about deprecated features.
# # EncodingWarning Base category for warnings about encoding issues.
# raise FutureWarning# Base category for warnings about constructs that will change semantically in the future.
# raise ImportWarning# Base category for warnings about probable mistakes in imports.
# raise PendingDeprecationWarning# Base category for warnings about features that will be deprecated in the future.
# raise ResourceWarning# Base category for warnings about resource usage issues.
# raise RuntimeWarning# Base category for warnings about suspicious runtime behavior.
# raise SyntaxWarning# Base category for warnings about dubious syntax.
# raise UnicodeWarning# Base category for warnings about Unicode-related issues.
# raise UserWarning# A warning category intended for user-defined warnings.  


'> Try-Except'
' > used for exception handling in python'

try:
    'Code Block that might raise an exception'

except:
    'Code Block to execute if the expection occurs'

#Handling specific errors

try:
    ...
except TypeError:
    ...
except ValueError:
    ...

try:
    ...
except Exception:
    ...
else:
    "Code Block to execute if no exception occurs"

try:
    ...
except Exception:
    ...
finally:
    'Code Block that always executes'