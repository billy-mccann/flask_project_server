Flask Project Server

I created a simple server to run locally to provide a backend for apps under development.

In the course of app development, there typically arises a point in time, shortly after the first of the UI framing has been laid out, that it would be nice to have data for the UI to display. 

There are a couple common ways developers like to populate this data. Stubbing out some mock data is always a popular option:

```swift

class Foo {
    static let MockFoo: Foo = ...
}

```
But, ultimately the app is typically going to end up fetching this data from *somewhere*. How nice would it be if there was somewhere to get it *now*, eeven if the backend is waiting on endpoints, or isn't built at all? For imags, the solution is typically to grab something from a public image API like https://placeholder.com/api/images/random, which is great because we don't have to keep a bunch of images on hand for mocking purposes. But what about everythign else in our data model, and what if the image url is inside of a larger data model (as is *always* the case). 

I'm going to show you an easy way to spin up a webserver that is always on hand. It's lightweight enough that you can keep it running in the background at all times, or you can easily start it and stop it with a single click.

---

## The webserver itself

I'm going to use Flask to spin up a quick and easy server written in Python. If you don't know Python, you can create your own server in Swift. But there are *so* many libaries and frameworks out there for Python that I'd encourage you to give it a shot. It's an easy language to pick up: it's highly intuitive and your first guess for syntax will, more often than not, be the right one.

---

## A simple home for your server to live in

Maybe, like me, you used Flask and Python to write your server. But what happens when you change development machines, and it doesn't have Flask, or a different version of Python, or no virtual environment? Or maybe you know javascript and you wrote your server with Node.js. What if you decided to give server-side Swift a shot and your server looks nothing like mine? Or your backend has multiple endpoints that facilitate different things? It would be *fantastic* if we didn't have to keep track of these differences, and know how to start a Flask app to serve some of our data, while a different Node.js server streaming out updates over a websocket. Thankfully, there is a solution, and it's called a *container*. 

A container is like a minimally-viable-everything-you-need in order to run your app (here, *app* is your server, and not your mobile application). Theoretically, it's not so different from an iPhone simulator. But whereas your iPhone simulator runs your app, a container will run your server. The magical part is that your container will work on your computer, my computer, a RaspberryPi, the Google Cloud Platform, a cluster of dusty old pcs that you built that one week when you got drunk and decided you weren't going to pay for cloud storage anymore...you get the picture. And you can start or stop the container with a mouse click. Going foward, whenever you need your development server, you can with trivial ease copy your container's image onto a new machine and *presto* you're up and running.

I'm going to use Docker as my containerization platform. You could use something else, but it's *probably* a boneheaded idea. Don't be a numbskull, just make it easy on yourself and use Docker.

## WOW that's really cool, where do I go from here?

Wherever you want king, the world is your oyster. If this simple server does everything you need to be of value in your app development, use it as is and get crackin' on those apps. If you feel as though you've just scratched the surface of something much bigger, then yeah. There's a **lot** more ice under the water here. You could spin up multiple containers: your server, maybe an image store, a redis cache, whatever you can dream up, dreamer. Then you could check out Docker-compose to get them working together. Or maybe you've dilly-dallied in the minors long enough and you're ready to go to the show: then it's time to check out Kubernetes (K8s). This is a choose-your-own-adventure type deal, time for baby bird to venture out beyond the nest. (That's you, you're baby bird. Go. Venture.)
