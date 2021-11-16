from flask import Flask,jsonify,render_template
from exchange import exchange
from getdata import corona, vaccine, kr_name, notice, noticeall
import json


app = Flask(__name__)
@app.route('/',methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/data',methods=['GET'])
def data():
    with open('./static/Test_json/api_data.json','r') as f:
        lvl_data = json.load(f)
    return jsonify({'caution':lvl_data})

'''
@app.route('/corona_data',methods=['GET'])
def data():
    with open('./coalarm_1.0/json_file/corona_data.json','r') as f:
        data = json.load(f)

    return jsonify({'result':'success','caution':data})

@app.route('/corona_vaccine_data',methods=['GET'])
def data():
    with open('./coalarm_1.0/json_file/corona_vaccine_data.json','r') as f:
        data = json.load(f)

    return jsonify({'result':'success','caution':data})

@app.route('/api_data',methods=['GET'])
def data():
    with open('./coalarm_1.0/json_file/api_data.json','r') as f:
        data = json.load(f)

    return jsonify({'result':'success','caution':data})
'''

    

@app.route('/country/<ISO_code>', methods=['GET'])
def country(ISO_code):
    # corona_data = Corona_data.query.filter(Coron_data.iso_code = ISO_code).first()
    # vaccine_data = Vaccine_data.query.filter(Vaccine_data.iso_code = ISO_code).first()
    # country_data = {'corona':corona_data,'vaccine':vaccine_data}
    exchange_rate = exchange(ISO_code)
    coronadata = corona(ISO_code)
    vaccinedata = vaccine(ISO_code)
    country_kr = kr_name(ISO_code)
    noticedata = notice(ISO_code)
    allnotice = noticeall(ISO_code)
    dataset = {
        'name':country_kr,'exchange':exchange_rate,'corona':coronadata,
        'vaccine':vaccinedata,'notice':noticedata,'allnotice':allnotice
        }
    return render_template('detail.html',data = dataset)

if __name__ =="__main__":
    app.run(debug=True)
