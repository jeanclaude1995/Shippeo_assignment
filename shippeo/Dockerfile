FROM python

#install poetry
RUN pip install poetry

# Copy the project files
COPY pyproject.toml poetry.lock ./

# Install the poetry dependencies 
RUN poetry install 

# Copy the rest of the project files
COPY app.py input_file.txt ./

# Run the application
CMD ["poetry", "run", "python", "app.py", "input_file.txt"]
