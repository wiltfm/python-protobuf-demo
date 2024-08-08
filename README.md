# Python Protobuf Demo

This project demonstrates how to use Protocol Buffers (protobuf) in a Python project.

## Description

Protocol Buffers (protobuf) is a method developed by Google for serializing structured data. It is useful in developing programs to communicate with each other over a network or for storing data.

## Installation

Clone the repository:
```sh
git clone https://github.com/wiltfm/python-protobuf-demo.git
cd python-protobuf-demo
```

Install the required dependencies:
```sh
make install
```

## Usage

Install protobuf:
```sh
brew install protobuf
```


To compile the `.proto` file:
```sh
protoc --python_out=. olympics.proto
```

To run:
```sh
make run
```
