load("@rules_python//python:py_binary.bzl", "py_binary")

# Bare minimal python script
py_binary(
   name="helloworld",
   srcs=["hello_world.py"],
   main="hello_world.py",
)

# Simple program for test without any external deps
py_binary(
   name="deep_thought",
   srcs=["deep_thought.py"],
   main="deep_thought.py",
   visibility=[":__subpackages__"],
)

# Simple program with single deps
py_binary(
    name = "cow_say",
    srcs = ["say.py"],
    main="say.py",
    deps = [
        "@pypi//cowsay",
    ],
)
