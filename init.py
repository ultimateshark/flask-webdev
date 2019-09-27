from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def Home():
	return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)



@app.route("/createnewcampaign",methods=["GET","POST"])
def createnewcampaign():
	try:
		if request.method=="POST":
			data=request.json
			ids=[]
			camp_type=data["selectedTypeval"]
			caption=data["caption"]
			app_token=data["uniquetoken"]
			link=data["link"]
			brand=Brand_details.query.filter_by(c_tokken=data["tokken"]).first()
			if data["fb"]:
				campaign=Campaign(name=data["name"],desc=data["description"],platform=0,creative_req=data["creativereq"],subtype=str(camp_type),linktoshare=link,caption=caption)
				db.session.add(campaign)
				brand.campaigns.append(campaign)
				db.session.commit()
				if int(camp_type) in [7,8]:
					for l in data["location"]:
						loc=Location.query.filter_by(location_id=int(l)).first()
						campaign.location.append(loc)
					db.session.commit()
				ids+=[campaign.campaign_id]
			if data["insta"]:
				campaign=Campaign(name=data["name"],desc=data["description"],platform=1,creative_req=data["creativereq"],subtype=str(camp_type),linktoshare=link,caption=caption)
				db.session.add(campaign)
				brand.campaigns.append(campaign)
				db.session.commit()
				if int(camp_type) in [7,8]:
					for l in data["location"]:
						loc=Location.query.filter_by(location_id=int(l)).first()
						campaign.location.append(loc)
					db.session.commit()
				ids+=[campaign.campaign_id]
			if data["yt"]:
				campaign=Campaign(name=data["name"],desc=data["description"],platform=2,creative_req=data["creativereq"],subtype=str(camp_type),linktoshare=link,caption=caption)
				db.session.add(campaign)
				brand.campaigns.append(campaign)
				db.session.commit()
				if int(camp_type) in [7,8]:
					for l in data["location"]:
						loc=Location.query.filter_by(location_id=int(l)).first()
						campaign.location.append(loc)
					db.session.commit()
				ids+=[campaign.campaign_id]
			if data["twitter"]:
				campaign=Campaign(name=data["name"],desc=data["description"],platform=3,creative_req=data["creativereq"],subtype=str(camp_type),linktoshare=link,caption=caption)
				db.session.add(campaign)
				brand.campaigns.append(campaign)
				db.session.commit()
				if int(camp_type) in [7,8]:
					for l in data["location"]:
						loc=Location.query.filter_by(location_id=int(l)).first()
						campaign.location.append(loc)
					db.session.commit()
				ids+=[campaign.campaign_id]
			if len(ids)==0:
				return jsonify(valid=False,err="No Platform Selected")
			db.session.commit()
			return jsonify(valid=True,msg="Campaign Created",campaign_ids=ids)
	except:
		return jsonify(valid=False,err="Something Went Wrong!!!")

