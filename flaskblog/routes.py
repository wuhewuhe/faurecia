import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask import jsonify

import random
from pyecharts import Scatter3D
from pyecharts import Bar
from pyecharts import Pie

import json
import pandas as pd
import numpy as np

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler



REMOTE_HOST = "https://pyecharts.github.io/assets/js"

aaaa = [{
    'author' : 'wuhe',
    'title' : 'Basic information',
    'content' : 'this is a dataset which is supported by the faurcia who is contributed in car accessoire, there are 10 thousands rows of data',
    'date_posted' : '2019.1.1'
},
{
    'author' : 'cuishuo',
    'title' : 'check',
    'content' : 'for our dataset, there are 8 attributes, and after our examen, there is no missing value',
    'date_posted' : '2019.1.2'
},{
    'author' : 'luozijian',
    'title' : 'introduction',
    'content' : 'Cycle time à It in the time (in seconds) that a product is done. Taking the first line, the part was injected in 58.8600 seconds' 
                 + 'Melt temperature à Temperature (in degrees Celsius) of the tool to melt the plastic to be injected' 
                 + 'Packing time à Time (in seconds) to inject the plastic in the tool to make the part' 
                 + 'Packing pressure à Pressure (in bar) of the injected plastic.' 
                 + 'Mold wall temperature à Tempreature (in degrees Celsius) of the tool where the plastic is injected.'
                 + 'Maximum injection pressure à Maximum pressure (in bar) achived during the injection process.' 
                 + 'Part weight à Weight (in gr) of the part after injection'
                 + 'Quality à OK if the part is valid and we deliver to the customer, and NOK scrap part, what is not valid and we need to discard it',
    'date_posted' : '2019.1.3'
}]

@app.route("/product")
def product():
# 主页面
    return render_template("product.html",title='Verify Prodouct')
   
@app.route('/add')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    c = request.args.get('c', 0, type=int)
    d = request.args.get('d', 0, type=int)
    e = request.args.get('e', 0, type=int)
    f = request.args.get('f', 0, type=int)
    g = request.args.get('g', 0, type=int)
    if a > 310  and b < 190 :
            return jsonify(result='NOK')
    else:
            return jsonify(result='OK')

   

@app.route('/boke')
def boke():
    data = {
        "data" : [
            {"Cycle_time":59,"Maximum_injection_pressure":301,"Melt_temperature":196,"Mold_wall_temperature":150,"Packing_pressure":96,"Packing_time":2,"Part_weight":302,"Quality":0,"Sequence":31},
            {"Cycle_time":61,"Maximum_injection_pressure":298,"Melt_temperature":186,"Mold_wall_temperature":138,"Packing_pressure":96,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":411},
            {"Cycle_time":61,"Maximum_injection_pressure":289,"Melt_temperature":217,"Mold_wall_temperature":148,"Packing_pressure":97,"Packing_time":2,"Part_weight":300,"Quality":0,"Sequence":495},
            {"Cycle_time":61,"Maximum_injection_pressure":307,"Melt_temperature":208,"Mold_wall_temperature":146,"Packing_pressure":113,"Packing_time":2,"Part_weight":291,"Quality":0,"Sequence":548},
            {"Cycle_time":62,"Maximum_injection_pressure":292,"Melt_temperature":200,"Mold_wall_temperature":148,"Packing_pressure":86,"Packing_time":2,"Part_weight":317,"Quality":0,"Sequence":555},
            {"Cycle_time":59,"Maximum_injection_pressure":303,"Melt_temperature":201,"Mold_wall_temperature":151,"Packing_pressure":103,"Packing_time":2,"Part_weight":282,"Quality":0,"Sequence":592},{"Cycle_time":60,"Maximum_injection_pressure":309,"Melt_temperature":210,"Mold_wall_temperature":143,"Packing_pressure":88,"Packing_time":2,"Part_weight":289,"Quality":0,"Sequence":670},
            {"Cycle_time":59,"Maximum_injection_pressure":306,"Melt_temperature":196,"Mold_wall_temperature":134,"Packing_pressure":109,"Packing_time":2,"Part_weight":306,"Quality":0,"Sequence":727},{"Cycle_time":61,"Maximum_injection_pressure":311,"Melt_temperature":201,"Mold_wall_temperature":163,"Packing_pressure":101,"Packing_time":2,"Part_weight":292,"Quality":0,"Sequence":923},
            {"Cycle_time":60,"Maximum_injection_pressure":292,"Melt_temperature":192,"Mold_wall_temperature":147,"Packing_pressure":104,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":950},{"Cycle_time":60,"Maximum_injection_pressure":288,"Melt_temperature":190,"Mold_wall_temperature":154,"Packing_pressure":104,"Packing_time":2,"Part_weight":301,"Quality":0,"Sequence":1226},
            {"Cycle_time":60,"Maximum_injection_pressure":310,"Melt_temperature":209,"Mold_wall_temperature":154,"Packing_pressure":104,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":1287},
            {"Cycle_time":61,"Maximum_injection_pressure":288,"Melt_temperature":205,"Mold_wall_temperature":160,"Packing_pressure":95,"Packing_time":2,"Part_weight":290,"Quality":0,"Sequence":1308},{"Cycle_time":61,"Maximum_injection_pressure":290,"Melt_temperature":193,"Mold_wall_temperature":163,"Packing_pressure":95,"Packing_time":2,"Part_weight":290,"Quality":0,"Sequence":1333},
            {"Cycle_time":62,"Maximum_injection_pressure":306,"Melt_temperature":196,"Mold_wall_temperature":152,"Packing_pressure":101,"Packing_time":2,"Part_weight":296,"Quality":0,"Sequence":1374},
            {"Cycle_time":61,"Maximum_injection_pressure":308,"Melt_temperature":183,"Mold_wall_temperature":146,"Packing_pressure":82,"Packing_time":2,"Part_weight":310,"Quality":0,"Sequence":1416},{"Cycle_time":60,"Maximum_injection_pressure":290,"Melt_temperature":217,"Mold_wall_temperature":154,"Packing_pressure":110,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":1431},{"Cycle_time":60,"Maximum_injection_pressure":310,"Melt_temperature":213,"Mold_wall_temperature":165,"Packing_pressure":109,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":1460},{"Cycle_time":61,"Maximum_injection_pressure":297,"Melt_temperature":202,"Mold_wall_temperature":146,"Packing_pressure":85,"Packing_time":2,"Part_weight":300,"Quality":0,"Sequence":1611},{"Cycle_time":60,"Maximum_injection_pressure":317,"Melt_temperature":195,"Mold_wall_temperature":156,"Packing_pressure":115,"Packing_time":2,"Part_weight":281,"Quality":0,"Sequence":1661},{"Cycle_time":60,"Maximum_injection_pressure":309,"Melt_temperature":214,"Mold_wall_temperature":141,"Packing_pressure":95,"Packing_time":2,"Part_weight":296,"Quality":0,"Sequence":1675},{"Cycle_time":60,"Maximum_injection_pressure":316,"Melt_temperature":214,"Mold_wall_temperature":155,"Packing_pressure":103,"Packing_time":2,"Part_weight":296,"Quality":0,"Sequence":2039},{"Cycle_time":59,"Maximum_injection_pressure":319,"Melt_temperature":202,"Mold_wall_temperature":157,"Packing_pressure":94,"Packing_time":2,"Part_weight":292,"Quality":0,"Sequence":2088},{"Cycle_time":60,"Maximum_injection_pressure":294,"Melt_temperature":190,"Mold_wall_temperature":150,"Packing_pressure":104,"Packing_time":2,"Part_weight":302,"Quality":0,"Sequence":2227},{"Cycle_time":61,"Maximum_injection_pressure":299,"Melt_temperature":207,"Mold_wall_temperature":162,"Packing_pressure":94,"Packing_time":2,"Part_weight":295,"Quality":0,"Sequence":2244},
            {"Cycle_time":60,"Maximum_injection_pressure":295,"Melt_temperature":212,"Mold_wall_temperature":158,"Packing_pressure":100,"Packing_time":2,"Part_weight":291,"Quality":0,"Sequence":2397},{"Cycle_time":61,"Maximum_injection_pressure":280,"Melt_temperature":194,"Mold_wall_temperature":146,"Packing_pressure":88,"Packing_time":2,"Part_weight":305,"Quality":0,"Sequence":2408},
            {"Cycle_time":61,"Maximum_injection_pressure":286,"Melt_temperature":198,"Mold_wall_temperature":136,"Packing_pressure":104,"Packing_time":2,"Part_weight":310,"Quality":0,"Sequence":2449},{"Cycle_time":61,"Maximum_injection_pressure":292,"Melt_temperature":209,"Mold_wall_temperature":139,"Packing_pressure":87,"Packing_time":2,"Part_weight":291,"Quality":0,"Sequence":2459},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":208,"Mold_wall_temperature":147,"Packing_pressure":105,"Packing_time":2,"Part_weight":301,"Quality":0,"Sequence":2738},{"Cycle_time":60,"Maximum_injection_pressure":315,"Melt_temperature":186,"Mold_wall_temperature":151,"Packing_pressure":102,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":2801},{"Cycle_time":60,"Maximum_injection_pressure":299,"Melt_temperature":198,"Mold_wall_temperature":161,"Packing_pressure":96,"Packing_time":2,"Part_weight":306,"Quality":0,"Sequence":2875},{"Cycle_time":61,"Maximum_injection_pressure":319,"Melt_temperature":195,"Mold_wall_temperature":148,"Packing_pressure":96,"Packing_time":2,"Part_weight":297,"Quality":0,"Sequence":3032},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":215,"Mold_wall_temperature":142,"Packing_pressure":113,"Packing_time":2,"Part_weight":292,"Quality":0,"Sequence":3099},{"Cycle_time":60,"Maximum_injection_pressure":302,"Melt_temperature":204,"Mold_wall_temperature":135,"Packing_pressure":90,"Packing_time":2,"Part_weight":294,"Quality":0,"Sequence":3174},{"Cycle_time":59,"Maximum_injection_pressure":282,"Melt_temperature":188,"Mold_wall_temperature":157,"Packing_pressure":109,"Packing_time":2,"Part_weight":311,"Quality":0,"Sequence":3272},{"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":200,"Mold_wall_temperature":153,"Packing_pressure":96,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":3275},{"Cycle_time":60,"Maximum_injection_pressure":302,"Melt_temperature":205,"Mold_wall_temperature":158,"Packing_pressure":109,"Packing_time":2,"Part_weight":313,"Quality":0,"Sequence":3364},{"Cycle_time":60,"Maximum_injection_pressure":288,"Melt_temperature":206,"Mold_wall_temperature":147,"Packing_pressure":88,"Packing_time":2,"Part_weight":281,"Quality":0,"Sequence":3423},{"Cycle_time":61,"Maximum_injection_pressure":294,"Melt_temperature":204,"Mold_wall_temperature":154,"Packing_pressure":104,"Packing_time":2,"Part_weight":310,"Quality":0,"Sequence":3598},{"Cycle_time":59,"Maximum_injection_pressure":291,"Melt_temperature":190,"Mold_wall_temperature":152,"Packing_pressure":87,"Packing_time":2,"Part_weight":296,"Quality":0,"Sequence":3691},{"Cycle_time":59,"Maximum_injection_pressure":289,"Melt_temperature":185,"Mold_wall_temperature":160,"Packing_pressure":113,"Packing_time":2,"Part_weight":306,"Quality":0,"Sequence":3980},{"Cycle_time":59,"Maximum_injection_pressure":296,"Melt_temperature":192,"Mold_wall_temperature":150,"Packing_pressure":88,"Packing_time":2,"Part_weight":298,"Quality":0,"Sequence":4032},{"Cycle_time":61,"Maximum_injection_pressure":306,"Melt_temperature":208,"Mold_wall_temperature":159,"Packing_pressure":81,"Packing_time":2,"Part_weight":310,"Quality":0,"Sequence":4142},{"Cycle_time":61,"Maximum_injection_pressure":294,"Melt_temperature":207,"Mold_wall_temperature":161,"Packing_pressure":94,"Packing_time":2,"Part_weight":304,"Quality":0,"Sequence":4294},{"Cycle_time":60,"Maximum_injection_pressure":303,"Melt_temperature":210,"Mold_wall_temperature":140,"Packing_pressure":106,"Packing_time":2,"Part_weight":285,"Quality":0,"Sequence":4393},{"Cycle_time":60,"Maximum_injection_pressure":306,"Melt_temperature":201,"Mold_wall_temperature":148,"Packing_pressure":90,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":4614},{"Cycle_time":59,"Maximum_injection_pressure":290,"Melt_temperature":200,"Mold_wall_temperature":149,"Packing_pressure":104,"Packing_time":2,"Part_weight":315,"Quality":0,"Sequence":4721},{"Cycle_time":60,"Maximum_injection_pressure":306,"Melt_temperature":214,"Mold_wall_temperature":140,"Packing_pressure":102,"Packing_time":2,"Part_weight":289,"Quality":0,"Sequence":4836},{"Cycle_time":58,"Maximum_injection_pressure":303,"Melt_temperature":196,"Mold_wall_temperature":152,"Packing_pressure":98,"Packing_time":2,"Part_weight":293,"Quality":0,"Sequence":4891},{"Cycle_time":60,"Maximum_injection_pressure":312,"Melt_temperature":215,"Mold_wall_temperature":158,"Packing_pressure":81,"Packing_time":2,"Part_weight":290,"Quality":0,"Sequence":4929},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":189,"Mold_wall_temperature":152,"Packing_pressure":100,"Packing_time":2,"Part_weight":302,"Quality":0,"Sequence":5201},{"Cycle_time":58,"Maximum_injection_pressure":303,"Melt_temperature":197,"Mold_wall_temperature":151,"Packing_pressure":113,"Packing_time":2,"Part_weight":317,"Quality":0,"Sequence":5314},{"Cycle_time":60,"Maximum_injection_pressure":306,"Melt_temperature":195,"Mold_wall_temperature":160,"Packing_pressure":100,"Packing_time":2,"Part_weight":298,"Quality":0,"Sequence":5512},{"Cycle_time":61,"Maximum_injection_pressure":291,"Melt_temperature":199,"Mold_wall_temperature":157,"Packing_pressure":100,"Packing_time":2,"Part_weight":309,"Quality":0,"Sequence":5614},{"Cycle_time":60,"Maximum_injection_pressure":298,"Melt_temperature":203,"Mold_wall_temperature":143,"Packing_pressure":115,"Packing_time":2,"Part_weight":318,"Quality":0,"Sequence":5749},{"Cycle_time":59,"Maximum_injection_pressure":295,"Melt_temperature":204,"Mold_wall_temperature":157,"Packing_pressure":117,"Packing_time":2,"Part_weight":315,"Quality":0,"Sequence":5852},{"Cycle_time":61,"Maximum_injection_pressure":294,"Melt_temperature":194,"Mold_wall_temperature":153,"Packing_pressure":90,"Packing_time":2,"Part_weight":308,"Quality":0,"Sequence":5956},{"Cycle_time":59,"Maximum_injection_pressure":283,"Melt_temperature":200,"Mold_wall_temperature":160,"Packing_pressure":108,"Packing_time":2,"Part_weight":289,"Quality":0,"Sequence":6387},{"Cycle_time":58,"Maximum_injection_pressure":303,"Melt_temperature":204,"Mold_wall_temperature":156,"Packing_pressure":90,"Packing_time":2,"Part_weight":299,"Quality":0,"Sequence":6499},{"Cycle_time":60,"Maximum_injection_pressure":315,"Melt_temperature":196,"Mold_wall_temperature":167,"Packing_pressure":101,"Packing_time":2,"Part_weight":307,"Quality":0,"Sequence":6554},{"Cycle_time":61,"Maximum_injection_pressure":285,"Melt_temperature":184,"Mold_wall_temperature":148,"Packing_pressure":104,"Packing_time":2,"Part_weight":283,"Quality":0,"Sequence":6821},{"Cycle_time":59,"Maximum_injection_pressure":293,"Melt_temperature":199,"Mold_wall_temperature":149,"Packing_pressure":110,"Packing_time":2,"Part_weight":303,"Quality":0,"Sequence":6850},{"Cycle_time":60,"Maximum_injection_pressure":296,"Melt_temperature":200,"Mold_wall_temperature":167,"Packing_pressure":89,"Packing_time":2,"Part_weight":293,"Quality":0,"Sequence":7103},{"Cycle_time":60,"Maximum_injection_pressure":305,"Melt_temperature":204,"Mold_wall_temperature":144,"Packing_pressure":95,"Packing_time":2,"Part_weight":308,"Quality":0,"Sequence":7271},{"Cycle_time":59,"Maximum_injection_pressure":291,"Melt_temperature":187,"Mold_wall_temperature":144,"Packing_pressure":95,"Packing_time":2,"Part_weight":302,"Quality":0,"Sequence":7423},{"Cycle_time":59,"Maximum_injection_pressure":299,"Melt_temperature":206,"Mold_wall_temperature":154,"Packing_pressure":110,"Packing_time":2,"Part_weight":287,"Quality":0,"Sequence":7438},{"Cycle_time":61,"Maximum_injection_pressure":290,"Melt_temperature":217,"Mold_wall_temperature":156,"Packing_pressure":97,"Packing_time":2,"Part_weight":295,"Quality":0,"Sequence":7677},{"Cycle_time":61,"Maximum_injection_pressure":313,"Melt_temperature":200,"Mold_wall_temperature":159,"Packing_pressure":89,"Packing_time":2,"Part_weight":301,"Quality":0,"Sequence":7942},{"Cycle_time":61,"Maximum_injection_pressure":300,"Melt_temperature":192,"Mold_wall_temperature":150,"Packing_pressure":90,"Packing_time":2,"Part_weight":319,"Quality":0,"Sequence":8322},{"Cycle_time":61,"Maximum_injection_pressure":314,"Melt_temperature":206,"Mold_wall_temperature":148,"Packing_pressure":100,"Packing_time":2,"Part_weight":298,"Quality":0,"Sequence":8823},{"Cycle_time":61,"Maximum_injection_pressure":298,"Melt_temperature":205,"Mold_wall_temperature":148,"Packing_pressure":108,"Packing_time":2,"Part_weight":316,"Quality":0,"Sequence":8884},{"Cycle_time":60,"Maximum_injection_pressure":285,"Melt_temperature":194,"Mold_wall_temperature":154,"Packing_pressure":106,"Packing_time":2,"Part_weight":288,"Quality":0,"Sequence":8946},{"Cycle_time":59,"Maximum_injection_pressure":294,"Melt_temperature":215,"Mold_wall_temperature":152,"Packing_pressure":100,"Packing_time":2,"Part_weight":300,"Quality":0,"Sequence":8996},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":219,"Mold_wall_temperature":158,"Packing_pressure":114,"Packing_time":2,"Part_weight":303,"Quality":0,"Sequence":9021},{"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":193,"Mold_wall_temperature":149,"Packing_pressure":97,"Packing_time":2,"Part_weight":298,"Quality":0,"Sequence":9611},{"Cycle_time":59,"Maximum_injection_pressure":298,"Melt_temperature":185,"Mold_wall_temperature":142,"Packing_pressure":83,"Packing_time":2,"Part_weight":300,"Quality":0,"Sequence":9644},
            {"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":204,"Mold_wall_temperature":155,"Packing_pressure":100,"Packing_time":2,"Part_weight":291,"Quality":0,"Sequence":9692},{"Cycle_time":61,"Maximum_injection_pressure":294,"Melt_temperature":219,"Mold_wall_temperature":153,"Packing_pressure":99,"Packing_time":2,"Part_weight":303,"Quality":0,"Sequence":9705}
            ]
    }
    return jsonify(data)

@app.route('/show')
def show():
    data = {
        "data" : [
        {"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":187,"Mold_wall_temperature":151,"Packing_pressure":88,"Packing_time":2,"Part_weight":292,"Quality":1,"Sequence":9791},
        {"Cycle_time":59,"Maximum_injection_pressure":287,"Melt_temperature":192,"Mold_wall_temperature":164,"Packing_pressure":101,"Packing_time":2,"Part_weight":303,"Quality":1,"Sequence":4143},{"Cycle_time":59,"Maximum_injection_pressure":302,"Melt_temperature":199,"Mold_wall_temperature":146,"Packing_pressure":93,"Packing_time":2,"Part_weight":310,"Quality":1,"Sequence":9201},{"Cycle_time":61,"Maximum_injection_pressure":313,"Melt_temperature":190,"Mold_wall_temperature":154,"Packing_pressure":96,"Packing_time":2,"Part_weight":314,"Quality":1,"Sequence":7161},
        {"Cycle_time":60,"Maximum_injection_pressure":307,"Melt_temperature":205,"Mold_wall_temperature":154,"Packing_pressure":86,"Packing_time":2,"Part_weight":310,"Quality":1,"Sequence":7364},{"Cycle_time":59,"Maximum_injection_pressure":303,"Melt_temperature":202,"Mold_wall_temperature":146,"Packing_pressure":116,"Packing_time":2,"Part_weight":283,"Quality":1,"Sequence":9486},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":199,"Mold_wall_temperature":145,"Packing_pressure":100,"Packing_time":2,"Part_weight":319,"Quality":1,"Sequence":3578},{"Cycle_time":61,"Maximum_injection_pressure":313,"Melt_temperature":195,"Mold_wall_temperature":150,"Packing_pressure":103,"Packing_time":2,"Part_weight":310,"Quality":1,"Sequence":7054},{"Cycle_time":61,"Maximum_injection_pressure":303,"Melt_temperature":189,"Mold_wall_temperature":149,"Packing_pressure":97,"Packing_time":2,"Part_weight":301,"Quality":1,"Sequence":3171},{"Cycle_time":60,"Maximum_injection_pressure":302,"Melt_temperature":211,"Mold_wall_temperature":151,"Packing_pressure":112,"Packing_time":2,"Part_weight":298,"Quality":1,"Sequence":7888},{"Cycle_time":60,"Maximum_injection_pressure":307,"Melt_temperature":197,"Mold_wall_temperature":143,"Packing_pressure":92,"Packing_time":2,"Part_weight":312,"Quality":1,"Sequence":8001},{"Cycle_time":61,"Maximum_injection_pressure":293,"Melt_temperature":200,"Mold_wall_temperature":141,"Packing_pressure":90,"Packing_time":2,"Part_weight":297,"Quality":1,"Sequence":3065},{"Cycle_time":59,"Maximum_injection_pressure":306,"Melt_temperature":208,"Mold_wall_temperature":162,"Packing_pressure":84,"Packing_time":2,"Part_weight":293,"Quality":1,"Sequence":7025},{"Cycle_time":60,"Maximum_injection_pressure":307,"Melt_temperature":195,"Mold_wall_temperature":163,"Packing_pressure":103,"Packing_time":2,"Part_weight":315,"Quality":1,"Sequence":2067},{"Cycle_time":61,"Maximum_injection_pressure":295,"Melt_temperature":199,"Mold_wall_temperature":132,"Packing_pressure":91,"Packing_time":2,"Part_weight":305,"Quality":1,"Sequence":7033},
        {"Cycle_time":61,"Maximum_injection_pressure":298,"Melt_temperature":187,"Mold_wall_temperature":151,"Packing_pressure":101,"Packing_time":2,"Part_weight":299,"Quality":1,"Sequence":4129},{"Cycle_time":61,"Maximum_injection_pressure":301,"Melt_temperature":204,"Mold_wall_temperature":140,"Packing_pressure":100,"Packing_time":2,"Part_weight":306,"Quality":1,"Sequence":830},{"Cycle_time":61,"Maximum_injection_pressure":298,"Melt_temperature":194,"Mold_wall_temperature":135,"Packing_pressure":105,"Packing_time":2,"Part_weight":299,"Quality":1,"Sequence":3586},{"Cycle_time":59,"Maximum_injection_pressure":302,"Melt_temperature":202,"Mold_wall_temperature":152,"Packing_pressure":93,"Packing_time":2,"Part_weight":301,"Quality":1,"Sequence":1067},{"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":206,"Mold_wall_temperature":136,"Packing_pressure":99,"Packing_time":2,"Part_weight":287,"Quality":1,"Sequence":6352},{"Cycle_time":60,"Maximum_injection_pressure":302,"Melt_temperature":183,"Mold_wall_temperature":161,"Packing_pressure":120,"Packing_time":2,"Part_weight":302,"Quality":1,"Sequence":6066},{"Cycle_time":60,"Maximum_injection_pressure":311,"Melt_temperature":197,"Mold_wall_temperature":154,"Packing_pressure":115,"Packing_time":2,"Part_weight":299,"Quality":1,"Sequence":2439},{"Cycle_time":62,"Maximum_injection_pressure":300,"Melt_temperature":209,"Mold_wall_temperature":154,"Packing_pressure":113,"Packing_time":2,"Part_weight":294,"Quality":1,"Sequence":8809},{"Cycle_time":61,"Maximum_injection_pressure":306,"Melt_temperature":207,"Mold_wall_temperature":165,"Packing_pressure":114,"Packing_time":2,"Part_weight":292,"Quality":1,"Sequence":8184},{"Cycle_time":59,"Maximum_injection_pressure":288,"Melt_temperature":183,"Mold_wall_temperature":159,"Packing_pressure":82,"Packing_time":2,"Part_weight":286,"Quality":1,"Sequence":3803},{"Cycle_time":60,"Maximum_injection_pressure":289,"Melt_temperature":191,"Mold_wall_temperature":147,"Packing_pressure":100,"Packing_time":2,"Part_weight":282,"Quality":1,"Sequence":9691},{"Cycle_time":60,"Maximum_injection_pressure":319,"Melt_temperature":207,"Mold_wall_temperature":159,"Packing_pressure":87,"Packing_time":2,"Part_weight":318,"Quality":1,"Sequence":2185},{"Cycle_time":60,"Maximum_injection_pressure":316,"Melt_temperature":193,"Mold_wall_temperature":144,"Packing_pressure":103,"Packing_time":2,"Part_weight":292,"Quality":1,"Sequence":6579},{"Cycle_time":60,"Maximum_injection_pressure":307,"Melt_temperature":204,"Mold_wall_temperature":149,"Packing_pressure":96,"Packing_time":2,"Part_weight":296,"Quality":1,"Sequence":9811},
        {"Cycle_time":60,"Maximum_injection_pressure":294,"Melt_temperature":200,"Mold_wall_temperature":154,"Packing_pressure":97,"Packing_time":2,"Part_weight":284,"Quality":1,"Sequence":2895},{"Cycle_time":61,"Maximum_injection_pressure":305,"Melt_temperature":204,"Mold_wall_temperature":156,"Packing_pressure":106,"Packing_time":2,"Part_weight":284,"Quality":1,"Sequence":2008},{"Cycle_time":60,"Maximum_injection_pressure":307,"Melt_temperature":198,"Mold_wall_temperature":140,"Packing_pressure":103,"Packing_time":2,"Part_weight":319,"Quality":1,"Sequence":2934},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":196,"Mold_wall_temperature":152,"Packing_pressure":88,"Packing_time":2,"Part_weight":312,"Quality":1,"Sequence":3602},{"Cycle_time":60,"Maximum_injection_pressure":293,"Melt_temperature":203,"Mold_wall_temperature":142,"Packing_pressure":105,"Packing_time":2,"Part_weight":309,"Quality":1,"Sequence":3783},{"Cycle_time":60,"Maximum_injection_pressure":287,"Melt_temperature":212,"Mold_wall_temperature":160,"Packing_pressure":101,"Packing_time":2,"Part_weight":295,"Quality":1,"Sequence":684},{"Cycle_time":60,"Maximum_injection_pressure":297,"Melt_temperature":197,"Mold_wall_temperature":137,"Packing_pressure":98,"Packing_time":2,"Part_weight":314,"Quality":1,"Sequence":1051},{"Cycle_time":61,"Maximum_injection_pressure":307,"Melt_temperature":188,"Mold_wall_temperature":145,"Packing_pressure":84,"Packing_time":2,"Part_weight":307,"Quality":1,"Sequence":3982},{"Cycle_time":59,"Maximum_injection_pressure":310,"Melt_temperature":219,"Mold_wall_temperature":138,"Packing_pressure":97,"Packing_time":2,"Part_weight":311,"Quality":1,"Sequence":5},{"Cycle_time":59,"Maximum_injection_pressure":288,"Melt_temperature":188,"Mold_wall_temperature":136,"Packing_pressure":103,"Packing_time":2,"Part_weight":305,"Quality":1,"Sequence":7356},{"Cycle_time":59,"Maximum_injection_pressure":290,"Melt_temperature":211,"Mold_wall_temperature":160,"Packing_pressure":94,"Packing_time":2,"Part_weight":284,"Quality":1,"Sequence":2305},{"Cycle_time":58,"Maximum_injection_pressure":298,"Melt_temperature":191,"Mold_wall_temperature":150,"Packing_pressure":99,"Packing_time":2,"Part_weight":305,"Quality":1,"Sequence":6391},{"Cycle_time":60,"Maximum_injection_pressure":306,"Melt_temperature":192,"Mold_wall_temperature":152,"Packing_pressure":114,"Packing_time":2,"Part_weight":298,"Quality":1,"Sequence":1314},{"Cycle_time":58,"Maximum_injection_pressure":293,"Melt_temperature":205,"Mold_wall_temperature":166,"Packing_pressure":101,"Packing_time":2,"Part_weight":307,"Quality":1,"Sequence":3642},{"Cycle_time":59,"Maximum_injection_pressure":306,"Melt_temperature":184,"Mold_wall_temperature":157,"Packing_pressure":95,"Packing_time":2,"Part_weight":289,"Quality":1,"Sequence":1510},{"Cycle_time":60,"Maximum_injection_pressure":309,"Melt_temperature":208,"Mold_wall_temperature":154,"Packing_pressure":111,"Packing_time":2,"Part_weight":309,"Quality":1,"Sequence":6158},{"Cycle_time":60,"Maximum_injection_pressure":313,"Melt_temperature":197,"Mold_wall_temperature":159,"Packing_pressure":90,"Packing_time":2,"Part_weight":287,"Quality":1,"Sequence":7721},{"Cycle_time":60,"Maximum_injection_pressure":302,"Melt_temperature":208,"Mold_wall_temperature":151,"Packing_pressure":103,"Packing_time":2,"Part_weight":307,"Quality":1,"Sequence":4507},{"Cycle_time":59,"Maximum_injection_pressure":289,"Melt_temperature":203,"Mold_wall_temperature":152,"Packing_pressure":101,"Packing_time":2,"Part_weight":303,"Quality":1,"Sequence":3026},{"Cycle_time":60,"Maximum_injection_pressure":299,"Melt_temperature":194,"Mold_wall_temperature":146,"Packing_pressure":87,"Packing_time":2,"Part_weight":302,"Quality":1,"Sequence":6432},{"Cycle_time":59,"Maximum_injection_pressure":296,"Melt_temperature":197,"Mold_wall_temperature":149,"Packing_pressure":98,"Packing_time":2,"Part_weight":286,"Quality":1,"Sequence":2710},{"Cycle_time":61,"Maximum_injection_pressure":300,"Melt_temperature":195,"Mold_wall_temperature":152,"Packing_pressure":115,"Packing_time":2,"Part_weight":294,"Quality":1,"Sequence":3290},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":198,"Mold_wall_temperature":154,"Packing_pressure":109,"Packing_time":2,"Part_weight":286,"Quality":1,"Sequence":8442},{"Cycle_time":60,"Maximum_injection_pressure":287,"Melt_temperature":206,"Mold_wall_temperature":135,"Packing_pressure":86,"Packing_time":2,"Part_weight":296,"Quality":1,"Sequence":8458},{"Cycle_time":61,"Maximum_injection_pressure":300,"Melt_temperature":193,"Mold_wall_temperature":145,"Packing_pressure":104,"Packing_time":2,"Part_weight":302,"Quality":1,"Sequence":8306},{"Cycle_time":59,"Maximum_injection_pressure":281,"Melt_temperature":198,"Mold_wall_temperature":144,"Packing_pressure":102,"Packing_time":2,"Part_weight":316,"Quality":1,"Sequence":4956},{"Cycle_time":59,"Maximum_injection_pressure":303,"Melt_temperature":198,"Mold_wall_temperature":150,"Packing_pressure":95,"Packing_time":2,"Part_weight":298,"Quality":1,"Sequence":6464},{"Cycle_time":59,"Maximum_injection_pressure":296,"Melt_temperature":214,"Mold_wall_temperature":165,"Packing_pressure":110,"Packing_time":2,"Part_weight":298,"Quality":1,"Sequence":520},{"Cycle_time":59,"Maximum_injection_pressure":311,"Melt_temperature":188,"Mold_wall_temperature":142,"Packing_pressure":99,"Packing_time":2,"Part_weight":281,"Quality":1,"Sequence":5329},{"Cycle_time":59,"Maximum_injection_pressure":288,"Melt_temperature":198,"Mold_wall_temperature":168,"Packing_pressure":106,"Packing_time":2,"Part_weight":283,"Quality":1,"Sequence":8666},{"Cycle_time":60,"Maximum_injection_pressure":303,"Melt_temperature":188,"Mold_wall_temperature":153,"Packing_pressure":85,"Packing_time":2,"Part_weight":299,"Quality":1,"Sequence":2970},{"Cycle_time":60,"Maximum_injection_pressure":304,"Melt_temperature":209,"Mold_wall_temperature":157,"Packing_pressure":106,"Packing_time":2,"Part_weight":299,"Quality":1,"Sequence":8404},{"Cycle_time":61,"Maximum_injection_pressure":299,"Melt_temperature":208,"Mold_wall_temperature":152,"Packing_pressure":88,"Packing_time":2,"Part_weight":303,"Quality":1,"Sequence":7899},
        {"Cycle_time":61,"Maximum_injection_pressure":293,"Melt_temperature":201,"Mold_wall_temperature":143,"Packing_pressure":96,"Packing_time":2,"Part_weight":299,"Quality":1,"Sequence":5920},{"Cycle_time":59,"Maximum_injection_pressure":304,"Melt_temperature":205,"Mold_wall_temperature":153,"Packing_pressure":101,"Packing_time":2,"Part_weight":301,"Quality":1,"Sequence":6551},{"Cycle_time":59,"Maximum_injection_pressure":301,"Melt_temperature":208,"Mold_wall_temperature":140,"Packing_pressure":99,"Packing_time":2,"Part_weight":304,"Quality":1,"Sequence":690},{"Cycle_time":59,"Maximum_injection_pressure":308,"Melt_temperature":200,"Mold_wall_temperature":144,"Packing_pressure":90,"Packing_time":2,"Part_weight":305,"Quality":1,"Sequence":1358},{"Cycle_time":60,"Maximum_injection_pressure":295,"Melt_temperature":196,"Mold_wall_temperature":149,"Packing_pressure":91,"Packing_time":2,"Part_weight":291,"Quality":1,"Sequence":2471},{"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":188,"Mold_wall_temperature":151,"Packing_pressure":97,"Packing_time":2,"Part_weight":298,"Quality":1,"Sequence":6421},{"Cycle_time":61,"Maximum_injection_pressure":306,"Melt_temperature":199,"Mold_wall_temperature":152,"Packing_pressure":99,"Packing_time":2,"Part_weight":311,"Quality":1,"Sequence":2600},{"Cycle_time":58,"Maximum_injection_pressure":318,"Melt_temperature":190,"Mold_wall_temperature":151,"Packing_pressure":109,"Packing_time":2,"Part_weight":318,"Quality":1,"Sequence":2675},{"Cycle_time":61,"Maximum_injection_pressure":297,"Melt_temperature":214,"Mold_wall_temperature":159,"Packing_pressure":102,"Packing_time":2,"Part_weight":316,"Quality":1,"Sequence":492},{"Cycle_time":59,"Maximum_injection_pressure":304,"Melt_temperature":214,"Mold_wall_temperature":168,"Packing_pressure":102,"Packing_time":2,"Part_weight":296,"Quality":1,"Sequence":7505},{"Cycle_time":60,"Maximum_injection_pressure":293,"Melt_temperature":206,"Mold_wall_temperature":134,"Packing_pressure":106,"Packing_time":2,"Part_weight":312,"Quality":1,"Sequence":9898},{"Cycle_time":61,"Maximum_injection_pressure":289,"Melt_temperature":198,"Mold_wall_temperature":156,"Packing_pressure":93,"Packing_time":2,"Part_weight":300,"Quality":1,"Sequence":6562},{"Cycle_time":60,"Maximum_injection_pressure":297,"Melt_temperature":202,"Mold_wall_temperature":145,"Packing_pressure":90,"Packing_time":2,"Part_weight":304,"Quality":1,"Sequence":6272},{"Cycle_time":60,"Maximum_injection_pressure":311,"Melt_temperature":191,"Mold_wall_temperature":145,"Packing_pressure":84,"Packing_time":2,"Part_weight":287,"Quality":1,"Sequence":7419},
        {"Cycle_time":60,"Maximum_injection_pressure":304,"Melt_temperature":210,"Mold_wall_temperature":154,"Packing_pressure":98,"Packing_time":2,"Part_weight":311,"Quality":1,"Sequence":611},{"Cycle_time":60,"Maximum_injection_pressure":291,"Melt_temperature":190,"Mold_wall_temperature":149,"Packing_pressure":101,"Packing_time":2,"Part_weight":295,"Quality":1,"Sequence":8548},{"Cycle_time":59,"Maximum_injection_pressure":294,"Melt_temperature":205,"Mold_wall_temperature":151,"Packing_pressure":92,"Packing_time":2,"Part_weight":309,"Quality":1,"Sequence":7917},{"Cycle_time":61,"Maximum_injection_pressure":302,"Melt_temperature":204,"Mold_wall_temperature":151,"Packing_pressure":99,"Packing_time":2,"Part_weight":300,"Quality":1,"Sequence":3587},{"Cycle_time":60,"Maximum_injection_pressure":303,"Melt_temperature":205,"Mold_wall_temperature":136,"Packing_pressure":96,"Packing_time":2,"Part_weight":300,"Quality":1,"Sequence":1},{"Cycle_time":60,"Maximum_injection_pressure":284,"Melt_temperature":193,"Mold_wall_temperature":146,"Packing_pressure":101,"Packing_time":2,"Part_weight":308,"Quality":1,"Sequence":6772},{"Cycle_time":61,"Maximum_injection_pressure":293,"Melt_temperature":198,"Mold_wall_temperature":138,"Packing_pressure":110,"Packing_time":2,"Part_weight":300,"Quality":1,"Sequence":441},{"Cycle_time":61,"Maximum_injection_pressure":308,"Melt_temperature":192,"Mold_wall_temperature":141,"Packing_pressure":104,"Packing_time":2,"Part_weight":289,"Quality":1,"Sequence":5231},{"Cycle_time":62,"Maximum_injection_pressure":306,"Melt_temperature":205,"Mold_wall_temperature":149,"Packing_pressure":96,"Packing_time":2,"Part_weight":311,"Quality":1,"Sequence":4491},{"Cycle_time":61,"Maximum_injection_pressure":291,"Melt_temperature":212,"Mold_wall_temperature":166,"Packing_pressure":103,"Packing_time":2,"Part_weight":312,"Quality":1,"Sequence":7218},{"Cycle_time":61,"Maximum_injection_pressure":288,"Melt_temperature":199,"Mold_wall_temperature":142,"Packing_pressure":91,"Packing_time":2,"Part_weight":285,"Quality":1,"Sequence":8211},{"Cycle_time":60,"Maximum_injection_pressure":308,"Melt_temperature":201,"Mold_wall_temperature":140,"Packing_pressure":99,"Packing_time":2,"Part_weight":301,"Quality":1,"Sequence":4489},{"Cycle_time":61,"Maximum_injection_pressure":291,"Melt_temperature":196,"Mold_wall_temperature":141,"Packing_pressure":95,"Packing_time":2,"Part_weight":282,"Quality":1,"Sequence":1034},{"Cycle_time":60,"Maximum_injection_pressure":293,"Melt_temperature":207,"Mold_wall_temperature":164,"Packing_pressure":85,"Packing_time":2,"Part_weight":292,"Quality":1,"Sequence":2919},{"Cycle_time":59,"Maximum_injection_pressure":298,"Melt_temperature":201,"Mold_wall_temperature":157,"Packing_pressure":104,"Packing_time":2,"Part_weight":301,"Quality":1,"Sequence":2285},{"Cycle_time":59,"Maximum_injection_pressure":290,"Melt_temperature":201,"Mold_wall_temperature":162,"Packing_pressure":88,"Packing_time":2,"Part_weight":298,"Quality":1,"Sequence":7877},{"Cycle_time":60,"Maximum_injection_pressure":300,"Melt_temperature":205,"Mold_wall_temperature":150,"Packing_pressure":105,"Packing_time":2,"Part_weight":319,"Quality":1,"Sequence":5713},{"Cycle_time":58,"Maximum_injection_pressure":297,"Melt_temperature":198,"Mold_wall_temperature":143,"Packing_pressure":107,"Packing_time":2,"Part_weight":290,"Quality":1,"Sequence":4551},{"Cycle_time":59,"Maximum_injection_pressure":292,"Melt_temperature":199,"Mold_wall_temperature":155,"Packing_pressure":118,"Packing_time":2,"Part_weight":299,"Quality":1,"Sequence":2488},
        {"Cycle_time":61,"Maximum_injection_pressure":305,"Melt_temperature":211,"Mold_wall_temperature":165,"Packing_pressure":93,"Packing_time":2,"Part_weight":299,"Quality":1,"Sequence":5728},{"Cycle_time":59,"Maximum_injection_pressure":293,"Melt_temperature":204,"Mold_wall_temperature":154,"Packing_pressure":108,"Packing_time":2,"Part_weight":303,"Quality":1,"Sequence":5069},{"Cycle_time":58,"Maximum_injection_pressure":304,"Melt_temperature":197,"Mold_wall_temperature":140,"Packing_pressure":85,"Packing_time":2,"Part_weight":301,"Quality":1,"Sequence":8127},{"Cycle_time":60,"Maximum_injection_pressure":301,"Melt_temperature":197,"Mold_wall_temperature":157,"Packing_pressure":116,"Packing_time":2,"Part_weight":287,"Quality":1,"Sequence":2209},
        {"Cycle_time":59,"Maximum_injection_pressure":299,"Melt_temperature":190,"Mold_wall_temperature":158,"Packing_pressure":101,"Packing_time":2,"Part_weight":297,"Quality":1,"Sequence":7368}
        ]
    }
    return jsonify(data)

@app.route('/aaa')
def aaa():
    #data = pd.read_json('quality.json')
    #data = data.to_json(orient='records')
    json_data=open(os.path.dirname(__file__)+'/static/quality.json')
    test=json.load(json_data)
    return jsonify(test)


@app.route('/mockup')
def mockup():
    #data = pd.read_json('quality.json')
    #data = data.to_json(orient='records')
    json_data=open(os.path.dirname(__file__)+'/static/faurecia.json')
    test=json.load(json_data)
    return jsonify(test)


@app.route('/dash/quality')
def quality():
    return render_template('quality.html')
    

@app.route('/dash/noquality')
def noquality():
  return render_template('noquality.html')

@app.route('/dash/management')
def management():
  return render_template('management.html')


@app.route("/echojson")
def echojson():  
    return render_template('echojson.html', title='faurecia')


@app.route("/visualisation")
def visualisation():
    s3d = scatter3d()
    return render_template('pyecharts.html',
                           myechart=s3d.render_embed(),
                           host=REMOTE_HOST,
                           script_list=s3d.get_js_dependencies())


def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D faurecia plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D


def generate_3d_random_point():
    return [random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 100)]

@app.route("/")
def faurecia():
    return render_template('faurecia.html', title='faurecia')

@app.route("/dash/statiscal")
def statiscal():
    return render_template('statiscal.html', title='result statiscal')

@app.route("/dash/distribution")
def distribution():
    return render_template('distribution.html', title='distribution')

@app.route("/dash/report")
def report():
    return render_template('report.html', title='report')

@app.route("/dash/choice")
def choice():
    return render_template('choice.html', title='choice')

@app.route("/dash/choice/cycle_time")
def result_pie_cycle():
    # s3d = scatter3d()
    return render_template('result_pie_cycle.html', title='PieChart')

@app.route("/dash/choice/barplot")
def result_barplot():
    return render_template('result_barplot.html', title='BarplotChart')

@app.route("/dash/choice/scatterplot")
def result_scatterplot():
    return render_template('result_scatterplot.html', title='ScatterplotChart')

@app.route("/dash/choice/radarplot")
def result_radarplot():
    return render_template('result_radarplot.html', title='radarplotChart')

@app.route("/dash")
def dash():
    df = pd.read_json('mockup.json')

    cols = df.select_dtypes(exclude=['float']).columns
    df[cols] = df[cols].apply(pd.to_numeric, downcast='float', errors='coerce')
    df = df.round(2)

    nb_sequence = df.describe()['Sequence']['count']
    avg_cycle = df.describe()['Cycle_time']['mean']
    avg_temperature = df.describe()['Melt_temperature']['mean']
    avg_pack = df.describe()['Packing_time']['mean']

    good=df['Quality'].value_counts()[1]
    bad=df['Quality'].value_counts()[0]

    print(nb_sequence)
    print(avg_cycle)
    print(avg_temperature)
    print(avg_pack)

    return render_template('dash.html',nb_sequence=nb_sequence,avg_cycle=avg_cycle,
                           avg_temperature=avg_temperature,avg_pack=avg_pack,
                           good=good,bad=bad)



@app.route("/pca_data")
def pca_data():
    df = pd.read_json('/Users/user/Desktop/Flask_Blog/mockup.json')
    df = df.drop(columns=['Sequence', 'Packing_time'])
    features = ['Cycle_time', 'Maximum_injection_pressure', 'Melt_temperature', 'Mold_wall_temperature','Packing_pressure','Part_weight']
    x = df.loc[:, features].values
    y = df.loc[:,['Quality']].values
    x = StandardScaler().fit_transform(x)
    test = pd.DataFrame(data = x, columns = features)
    test = test.iloc[0:100,:]
    #print(test)
    json_data=open(os.path.dirname(__file__)+'/static/quality.json')
    data=json.load(json_data)
    return jsonify(data)
   
@app.route("/pca")
def pca():
    return render_template('pca.html', title='pca')

@app.route("/pca_result")
def pca_result():
    return render_template('pca_result.html', title='pca_dimension')

@app.route("/pattern")
def pattern():
    return render_template('pattern.html', title='pattern')

@app.route("/create_chart")
def create_chart():
    bar = Bar("Analyst no quality data", "Maximum_injection_pressure range")
    bar.add("inject pressure", ["0--280", "280--290", "290--300", "300--310", "310--329"], [1, 14, 30, 24, 10], is_more_utils=True)
    bar.render()
    return render_template('pattern.html',
                           myechart=bar.render_embed(),
                           host=REMOTE_HOST,
                           script_list=bar.get_js_dependencies())

@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.asc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',image_file=image_file, form=form)

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')



@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)






