FROM heroku/miniconda:3

# Grab requirements.txt.
ADD ./webapp/requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install -qr /tmp/requirements.txt

RUN conda install scikit-learn pandas

# Add our code
ADD ./webapp /opt/webapp/
WORKDIR /opt/webapp

# Add our model
ADD ./clf.pkl /opt/webapp/

CMD gunicorn --log-level debug --timeout 120 --bind 0.0.0.0:$PORT wsgi
