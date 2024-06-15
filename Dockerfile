# Use the official Python 3.9 image
FROM python:3.9

# set working dir to /code
WORKDIR /code

# Copy the current dir content in the container at /code
COPY ./requirements.txt /code/requirements.txt

# Install the requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# set up a new user named "user"
RUN useradd user
# Switch the "user" as user
USER user

# set home to the user's home dir

ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# set the working dir to the user's home dir 
WORKDIR $HOME/app

# Copy the current Directory content into yhe container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

# Start the fastapi app on port 7860
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]