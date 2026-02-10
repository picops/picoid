from picobuild import Extension, cythonize, get_cython_build_dir, setup

extensions = cythonize(
    Extension(
        "cuuid.*",
        ["src/cuuid/*.pyx", "src/cuuid/uuid.c"],
        extra_compile_args=[
            "-O2",
            "-march=native",
            "-Wno-unused-function",
            "-Wno-unused-variable",
        ],
        language="c",
    ),
    compiler_directives={"language_level": 3},
    build_dir=get_cython_build_dir(),
)


if __name__ == "__main__":
    setup(
        name="cuuid",
        version="0.0.1",
        ext_modules=extensions,
    )
