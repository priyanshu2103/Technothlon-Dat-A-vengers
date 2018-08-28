from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import TableSet, Credits
from pandas.compat import StringIO
import json 
##############################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
import missingno as msno
import io
import base64
###############################################

def load_data_init_train():
	""" Creating the DataFrames """
	df = pd.read_csv("train_game.csv")
	df = pd.DataFrame(df)
	return df[0:300]

def load_data_test():
	""" Test Loading Initially """
	df = pd.read_csv("train_game.csv")
	df = pd.DataFrame(df)
	return df[1000:]

def to_pd(df):
	return pd.read_csv(StringIO(df), sep='\s+')

###################################### Extra Data #############################
def load_data_in_train(x1,x2,credits):
	""" Creating Dataframes with credits change """
	df = pd.read_csv("train_game.csv")
	df = pd.DataFrame(df)
	if(x2 >= 1001):
		#print("Dont cross your limits!!")
		return None
	cdf = df[x1:x2]
	credits -= ((x2 - x1) * 2)
	return cdf,credits

def append_data(df, x1 , x2 , credits):
	# Appending the Data
	extra_data,credits = load_data_in_train(x1,x2,credits)
	df = df.append(extra_data)
	return df,credits
################################ E D Done ########################################

################################# Null Checking ########################################


def see_null_each(df,credits):
	"""Nullity check """

	credits -= 100
	return credits

def null_sum(df,col_name,credits):
	""" Number of Null in Cols """
	credits -= 50
	return credits


def null_any(df,credits):
	""" Number of Columns having NULL """
	credits -= 300
	return credits


def check_null(df,input_val,credits,col_name = None ):
	""" Which Null to call """
	if(input_val == "columns_null"):
		credits = see_null_each(df,credits)
	elif(input_val == "total_null"):
		credits = null_sum(df,col_name,credits)
	else:
		credits = null_any(df,credits)
	return credits


##################################################### n c Done ###########################################
############################################ normalization ################################################

def better_normalization(df,col_name,credits):
	Normalization = 100
	credits = credits - Normalization
	df[col_name] = ((df[col_name] - df[col_name].mean())/df[col_name].std())
	return df,credits

def mean_normalization(df,col_name,credits):
	credits = credits - 50
	df[col_name] = (df[col_name] - df[col_name].mean())
	return df,credits

def std_normalization(df,col_name,credits):
	credits = credits - 20
	df[col_name] = df[col_name] / df[col_name].std()
	return df,credits 

 
def normalization(df,input_val,credits,col_name):
	""" Which Normalization to call """
	if(input_val == 1):
		df,credits = better_normalization(df,col_name,credits)
	elif(input_val == 2):
		df,credits = mean_normalization(df,col_name,credits)
	else:
		df,credits = std_normalization(df,col_name,credits)
	return df,credits
############################# nor done #######################################################################

########################################### graph data ##########################################################

def line(df,credits,col_name):
	""" Line Graph per column"""
	line = 50 
	credits = credits - line 
	return df[col_name].plot(kind = 'line'),credits

def histogram(df,credits , col_name):
	""" Histogram for Whole Data """
	hist = 500 
	credits = credits - hist 
	return df[col_name].plot(kind = 'hist'),credits

def draw_graph(df,credits,input_val,col_name ):
	""" Which Graph """
	if(input_val == 1):
		pl,credits = line(df,credits,col_name)
	else:
		pl,credits = histogram(df,credits , col_name)

	buf = io.BytesIO()
	plt.savefig(buf, format='png')
	image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
	buf.close()
	return image_base64, credits

#############################done graph #######################################################################

################################################# null graph ####################################################

def null_graph(df,credits,input_val):
	""" Which Missing No Grpah to Call """
	# Graphs are Sexy but are not very Sizzling Hot #
	if(input_val == 1):
		pl,credits = matrix(df,credits)
	elif(input_val == 2):
		pl,credits = heatmap(df,credits)
	elif(input_val == 3):
		pl,credits = dendrogram(df,credits)
	else:
		pl,credits = bar(df,credits)
	
	buf = io.BytesIO()
	plt.savefig(buf, format='png')
	image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')
	buf.close()
	return image_base64, credits


def matrix(df,credits):
 	matrix = 500
 	credits = credits - matrix
 	return matrix(df.sample(df.shape[0])),credits

def heatmap(df,credits):
 	heatmap = 400
 	credits = credits - heatmap
 	return heatmap(df.sample(df.shape[0])),credits	

def dendrogram(df,credits):
 	dendrogram = 400
 	credits = credits - dendrogram
 	return dendrogram(df.sample(df.shape[0])),credits

def bar(df,credits):
	bar = 700
	credits = credits - bar
	return bar(df.sample(df.shape[0])),credits

############################################ ng Done ############################################################## 
############################################# Fill null ###########################################################
def mean_null(df,credits,col_name):
	""" Fill NUll values with mean"""
	df[col_name] = df[col_name].fillna(df[col_name].mean())
	credits -= 400
	return df,credits

def zero_null(df,credits,col_name):
	""" Fill Null with 0's """
	df[col_name] = df[col_name].fillna(0)
	credits -= 100
	return df,credits

def std_null(df,credits,col_name):
	""" Fill NUll values with standard deviation """
	df[col_name] = df[col_name].fillna(df[col_name].std())
	credits -= 250
	return df,credits

def fill_null(df,credits,input_val,col_name):
	""" Which null filler to call """
	if(input_val == 1):
		df,credits = mean_null(df,credits,col_name)
	elif(input_val == 2):
		df,credits = zero_null(df,credits,col_name)
	else:
		df,credits = std_null(df,credits,col_name)

	return df,credits

############################################## f n done #########################################################


def Start(request):
	if request.user.is_authenticated:
		return render(request,'main/index.html',{'key':["cgghjghm","advdfv",5656,955,875],'sid':0})
	else:
		return HttpResponse("Not Logged IN")

def Index(request):

	if request.user.is_authenticated:
		data = TableSet.objects.filter(user=request.user.id).first()
		if data is None:
			df = load_data_init_train()
			cre = Credits()
			cre.user = request.user
			cre.save()
			dat = TableSet()
			dat.user = request.user
			dat.data = df.to_string()
			dat.save()
			return HttpResponse("Initialized")
		else:
			return HttpResponseRedirect('/start')
	else:
		return HttpResponseRedirect('/accounts/login/')

def View_1(request):
	if request.method=="POST":
		low = request.POST['low']
		high = request.POST['high']
		ts = TableSet.objects.filter(user=request.user.id).first()
		cr = Credits.objects.filter(user=request.user.id).first()
		credits = cr.credits
		df = to_pd(ts.data)
		df,credits = append_data(df,int(low),int(high),credits)
		ts.data = df.to_string()
		cr.credits = credits
		ts.save()
		cr.save()
		dic = {}
		dic['credit'] = credits
		dic['message'] = "Successful."
		return HttpResponse(json.dumps(dic))

def View_2(request):
	if request.method=="POST":
		store = ""
		input_val = request.POST['input_val']
		col = request.POST['col']
		ts = TableSet.objects.filter(user=request.user.id).first()
		cr = Credits.objects.filter(user=request.user.id).first()
		df = to_pd(ts.data)
		credits = cr.credits

		if input_val =="columns_null":
			credits = check_null(df,input_val,credits)
			pd.set_option('max_rows', 81)
			store = df.isna().any().to_dict()
		elif input_val =="total_null":
			credits = check_null(df,input_val,credits,col)
			store = str(df[col].isnull().sum())
		elif input_val =="t_c_null":
			credits = check_null(df,input_val,credits)
			store = int(df.isna().any().sum())
		
		ts.data = df.to_string()
		cr.credits = credits
		#ts.save()
		#cr.save()
		dic = {}
		dic['credit'] = credits
		dic['message'] = "Successful."
		dic['data'] =  store
		return JsonResponse(dic)



def View_3(request):
	if request.method=="POST":
		input_val = int(request.POST['input_val'])
		col = request.POST['col']
		ts = TableSet.objects.filter(user=request.user.id).first()
		cr = Credits.objects.filter(user=request.user.id).first()
		credits = cr.credits
		df = to_pd(ts.data)
		df,credits = normalization(df,input_val,credits,col )
		ts.data = df.to_string()
		cr.credits = credits
		#ts.save()
		#cr.save()
		dic = {}
		dic['credit'] = credits
		dic['message'] = "Successful."
		return HttpResponse(json.dumps(dic))



def View_4(request):
	if request.method=="POST":
		input_val = int( request.POST['input_val'])
		col = request.POST['col']
		ts = TableSet.objects.filter(user=request.user.id).first()
		cr = Credits.objects.filter(user=request.user.id).first()
		credits = cr.credits
		df = to_pd(ts.data)
		graph, credits = draw_graph(df,credits,input_val,col)
		ts.data = df.to_string()
		cr.credits = credits
		#ts.save()
		#cr.save()
		return HttpResponse(graph)
		dic = {}
		dic['credit'] = credits
		dic['message'] = "Successful."
		return HttpResponse(json.dumps(dic))

def View_5(request):
	if request.method=="POST":
		input_val = int(request.POST['input_val'])
		ts = TableSet.objects.filter(user=request.user.id).first()
		cr = Credits.objects.filter(user=request.user.id).first()
		credits = cr.credits
		df = to_pd(ts.data)
		graph , credits = null_graph(df,credits,input_val)
		ts.data = df.to_string()
		cr.credits = credits
		#ts.save()
		#cr.save()
		return HttpResponse(graph)
		dic = {}
		dic['credit'] = credits
		dic['message'] = "Successful."
		return HttpResponse(json.dumps(dic))


def View_6(request):
	if request.method=="POST":
		input_val = int(request.POST['input_val'])
		col = request.POST['col']
		ts = TableSet.objects.filter(user=request.user.id).first()
		cr = Credits.objects.filter(user=request.user.id).first()
		credits = cr.credits
		df = to_pd(ts.data)
		df,credits = fill_null(df,credits,input_val,col)
		ts.data = df.to_string()
		cr.credits = credits
		#ts.save()
		#cr.save()
		dic = {}
		dic['credit'] = credits
		dic['message'] = "Successful."
		return HttpResponse(json.dumps(dic))