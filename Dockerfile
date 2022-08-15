FROM  python:3.9.12
LABEL Author, Esteban Encina

WORKDIR /app
COPY requirements.txt ./requirements.txt
#---------------- Prepare the environment
## Install dependencies
RUN pip install -r requirements.txt
## Expose the app
EXPOSE 8501
COPY . /app
## Run the app
ENTRYPOINT [ "streamlit" , "run"]
CMD [ "front_end.py" ]
