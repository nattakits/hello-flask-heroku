from flask import Flask
from flask_jsonpify import jsonpify
from flask_restful import Resource,Api,reqparse
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!!!!'

api=Api(app)

@app.route('/')
def index():
    return "hello world"

class get_mathcal(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('input1',type=str)
        parser.add_argument('input2',type=str)
        parser.add_argument('input3',type=str)
        #parser.add_argument('operation',type=str)
        dictp=parser.parse_args()
        inp_1=dictp['input1']
        inp_2=dictp['input2']
        inp_3=dictp['input3']
        #oper=dictp['operation']
        #if(oper=='plus'):
            #oper='+'
        #else:
            #oper='-'
        inp_1=int(inp_1)
        inp_2=int(inp_2)
        inp_3=int(inp_3)
        inp1=inp_1*12+inp_2+inp_3-60000-100000
        print(inp1)
        if(int(inp1)<=150000):  #<150000
            inp1='0'+' '+'บาท'
        elif(int(inp1)<=300000): #150000-300000
            inp1=(int(inp1)-150000)*0.05
            inp1=str(round(inp1,2))+' '+'บาท'
        elif(int(inp1)<=500000):
            inp1=7500+(int(inp1)-300000)*0.10
            inp1=str(round(inp1,2))+' '+'บาท'
        elif(int(inp1)<=750000):
            inp1=7500+20000+(int(inp1)-500000)*0.15
            inp1=str(round(inp1,2))+' '+'บาท'
        elif(int(inp1)<=1000000):
            inp1=7500+20000+37500+(int(inp1)-750000)*0.20
            inp1=str(round(inp1,2))+' '+'บาท'
        elif(int(inp1)<=2000000):
            inp1=7500+20000+37500+50000+(int(inp1)-1000000)*0.25
            inp1=str(round(inp1,2))+' '+'บาท'
        elif(int(inp1)<=5000000):
            inp1=7500+20000+37500+50000+250000+(int(inp1)-2000000)*0.30
            inp1=str(round(inp1,2))+' '+'บาท'
        elif(int(inp1)>5000000):
            inp1=7500+20000+37500+50000+250000+900000+(int(inp1)-5000000)*0.30
            inp1=str(round(inp1,2))+' '+'บาท'

        

        stringcal=inp1
        
        
        print(stringcal)
        #answ = eval(stringcal)
        result={}
        result['stringcal']=stringcal
        #result['answer']=answ
        return(result)
api.add_resource(get_mathcal, '/cal',endpoint='cal')



if __name__ == '__main__':
    app.run()
