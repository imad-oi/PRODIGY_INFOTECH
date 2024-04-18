FROM python:3.7 

WORKDIR /app

RUN pip install pandas numpy scikit-learn matplotlib seaborn

ADD /models /models
ADD /data /data


EXPOSE 5000

CMD ["python", "app.py"]


# docker build -t prodigy_ml_01 
# docker run -p 5000:5000 prodigy_ml_01
