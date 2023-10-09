from flask import Flask,render_template,jsonify

app=Flask(__name__)

JOBS=[
    {"id":1,
     'title':"Data Analyst",
     'location':'Bangalore,Bharat',
     'salary':'Rs 100000'
    },
    {"id":2,
     'title':"Data Scientist",
     'location':'Delhi ,Bharat',
     'salary':'Rs 120000'
    },
    {"id":3,
     'title':"ML Engineer",
     'location':'Chennai,Bharat',
     'salary':'Rs 800000'
    },
    {"id":4,
     'title':"AI Engineer",
     'location':'Hyderbad,Bharat',
    }
]

@app.route('/')
def hello_world():
    return render_template('bootstrap.html',jobs=JOBS,company_name='VM')


## IF want this information relating job details in json format
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)