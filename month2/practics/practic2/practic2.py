#! Python3.11.4

# родительский класс - Дед
class Assembler:
    def __init__(self, filename: str,  memory: list, optimisation: bool = True, architecture: str = "x86",):
        self.architecture = architecture
        self.filename = filename
        self.optimisation = optimisation
        # защищенный атрибут
        self.__memory = memory

    def optimise(self, source_code):
        return "code was optimised"

    # получение защищенного атрибута (getter)
    @property
    def load_value(self, address:int=None):
        if not address:
            return self.__memory
        else:
            return self.__memory[address]
        
    # внесение значения в защищенный атрибут (setter)
    @load_value.setter
    def set_mem_value(self, address:int, value):
        if (address < (len(self.__memory)-1)):
            self.__memory.insert(address, value)

        elif (address > (len(self.__memory)-1)):
            self.__memory.append(value)
        
        else:
            raise TypeError("Something isn't right")

    def assemble(self, source_code):
        if self.optimisation:
            self.optimise(source_code)
        return source_code

    def compile_program(self, program):
        return f"Compiling program in {self.architecture} assembly language:\n{program}"

# класс потомок (отец)
class C(Assembler):
    def __init__(self, filename: str, memory: list, optimisation: bool = True, compiler: str = "gcc",):
        super().__init__(filename, optimisation, memory)
        self.compiler = compiler

    # def pointer_operation(self, operation, address, value=None):
    #     if 0 <= address < len(self.load_value):
    #         if operation == "read":
    #             return self.load_value[address]
    #         elif operation == "write":
    #             if value is not None:
    #                 self.set_mem_value[address] = value
    #                 return f"Value at address {address} updated to {value}"
    #             else:
    #                 raise ValueError("Error: No value provided for write operation.")
    #     else:
    #         raise IndexError("Error: Invalid memory address")

    def compile_program(self, program):
        return f"Compiling C program:\n{program} - with - {self.compiler}"
    
    def run_program(self, compiled_program):
        result = f"Running the following program:\n{compiled_program}"
        print(result)
        return result

# класс потомок-потомка (сын)
class CPP(C):
    def __init__(self, filename: str, optimisation: bool = True, memory: list = [0,0,0,0,0,] ,compiler: str = "clang", language: str = "C++"):
        super().__init__(filename, optimisation, memory, compiler,)
        self.language = language

    def object_oriented_programming(self):
        return f"Working on object-oriented programming in {self.language}"
    
    def compile_program(self, program):
        compiled_program = f"{self.filename}.exe"
        return f"Compiling C++ program: {self.language} program to {compiled_program} - with - {self.compiler}"
    
    def run_program(self, compiled_program):
        result = f"Running the following C++ program:\n{compiled_program}"
        print(result)
        return result

# Использование
# Создаем объект класса Assembler
print("********************\n")
assembler_instance = Assembler("program.asm", architecture="x86", memory=[0, 1, 2, 3, 4])

# Используем методы объекта Assembler
print(assembler_instance.assemble("source code for assembly"))
print(f"Memory Values: {assembler_instance.load_value}")
compiled_asm_program = assembler_instance.compile_program("Assembly program code")
print("\n********************\n")

# Создаем объект класса C
c_instance = C("program.c", memory=[5, 6, 7, 8, 9],compiler="gcc",)

# Используем методы объекта C
# print(c_instance.pointer_operation("read", 2))
# print(c_instance.pointer_operation("write", 3, 42))
print(f"Memory Values: {c_instance.load_value}")
compiled_c_program = c_instance.compile_program("C program code")
c_instance.run_program(compiled_c_program)
print("\n********************\n")

# Создаем объект класса CPP
cpp_instance = CPP("program.cpp", memory=[10, 11, 12, 13, 14], compiler="g++", language="C++")

# Используем методы объекта CPP
print(cpp_instance.run_program("compiled_program.exe"))
print(cpp_instance.object_oriented_programming())
print(f"Memory Values: {cpp_instance.load_value}")
compiled_cpp_program = cpp_instance.compile_program("C++ program code")
cpp_instance.run_program(compiled_cpp_program)
