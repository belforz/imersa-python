from cx_Freeze import setup, Executable

setup (
	name="Build",
	version="1.0",
	description ="Meu programa executavel",
	executables = [Executable("iszero.py")],

)
