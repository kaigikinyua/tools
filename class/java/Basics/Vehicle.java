class Vehicle{
	public String model;
	public int engineRevs;
	public int transMissionRatio;

	private int maxSpeed;
	Vehicle(String model,int engineRevs,int transMissionRatio){
		this.model=model;
		this.engineRevs=engineRevs;
		this.transMissionRatio=transMissionRatio;
	}
	//guessing how the maxSpeed is calculated;
	public int setMaxSpeed(){
		this.maxSpeed=(this.engineRevs*this.transMissionRatio)*(3.14*0.5)*(18/5);
		return maxSpeed;
	}
	
}