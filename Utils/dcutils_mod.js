function makeNumeric(s)
{
	return filterChars(s, "1234567890.-");
}

function numval(val,digits,minval,maxval)
{
	val = makeNumeric(val);
	if (val == "" || isNaN(val)) val = 0;
	val = parseFloat(val);
	if (digits != null)
	{
		var dec = Math.pow(10,digits);
		val = (Math.round(val * dec))/dec;
	}
	if (minval != null && val < minval) val = minval;
	if (maxval != null && val > maxval) val = maxval;
	return parseFloat(val);
}



function presentValue(fv,r,y)
{
	return fv/Math.pow(1+r,y);
}

function futureValue(p,r,y)
{
	return p*Math.pow(1+r,y);
}


function geomSeries(z,m,n)
{
	var amt;
	if (z == 1.0) amt = n + 1;
	else amt = (Math.pow(z,n + 1) - 1)/(z - 1);
	if (m >= 1) amt -= geomSeries(z,0,m-1);
	return amt;
}


function annuityPayout(p,r,y)
{
	return futureValue(p,r,y-1)/geomSeries(1+r,0,y-1);
}


