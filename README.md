### Bogus consultation

This script allows you to automatically fill in the [National Consultation](https://nemzetikonzultacio.kormany.hu/) of the Hungarian government with bullshit data.

This is a product of my outrage which is fueled by the narrowminded politicians we have in 2020.

The consultation is full of suggestive questions with only obvious answers for less educated people.

In order to run the script you need to do the following. Assuming you have python3.7 installed.

``` bash
git clone https://github.com/r3ap3rpy/bogusconsultation
cd bogusconsultation
pip install -r requirements.txt
```

Then issue how many participiants you want to fill the bullshit consultation.

``` bash
python bsconsulting.py -participiants 1000000
```

The script only supports around *5000000* participiants, which is like more than half of hungary's population.

It uses threading to accelerate the process aswell.

Under the sources you find an offline installer with which the *geckodriver* is compatible so you have no problems running it.

It only works on windows due to the source folders content, however you can adjust it for linux if you please.

At the end of a successfull session you will find something like this.

![success](/pics/success.PNG)