#!/bin/bash

echo "================================="
echo " PersonaDNA Development Check"
echo "================================="

echo
echo "Formatting..."
black src tests

echo
echo "Linting..."
ruff check src tests

echo
echo "Running Tests..."
pytest -v

echo
echo "Done."
