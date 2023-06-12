### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
**python is backend. Deals with server, handles gets and request.  javascript is frontend. Deals with UI and manipulating the DOM**

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
1.  
```python
d["c"] = 3  
print(d) 
```

2.  
```python
d.get("c", 3)
```




- What is a unit test?
**A test that tests 1 small peice of a app(like a function) at a time**

- What is an integration test?
*testing mutiple things in app toghether to see if they cohesivly work

- What is the role of web application framework, like Flask?
**tells you how and what to respond to**

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
**The RouteURl is used the main page, the basis of thr content. the query param is extra info within that content, it usually doenst need its own page**

- How do you collect data from a URL placeholder parameter using Flask?
using the root params

- How do you collect data from the query string using Flask?
  - request.args
  - request.args.get()

- How do you collect data from the body of the request using Flask?
  * requests.json.get();
  * request.form.get():

- What is a cookie and what kinds of things are they commonly used for?
**cookies are small peices of data that is stored in browser**

- What is the session object in Flask?
**Its a magic dictionary that stores info for current browser, perserves type and signed so user cant modify data**

- What does Flask's `jsonify()` do?
**makes data readable for frontend side**