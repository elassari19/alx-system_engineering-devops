# Secured and monitored web infrastructure
design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.

![](https://res.cloudinary.com/elassari/image/upload/v1698527737/alx/okaznb5z6oyqzybormgt.png)

## Requirements
  * 3 firewalls
  * 1 SSL certificate to serve www.foobar.com over HTTPS
  * 3 monitoring clients (data collector for Sumologic or other monitoring services)

## explain some specifics about this infrastructure
* #### For every additional element, why you are adding it
  every successful monitoring platform needs to have five essential components; identify, collect, share, integrate, and govern. Let's break down what each of those mean.

  * Identify
  * Collect
  * Share
  * Integrate
  * Govern

* #### What are firewalls for
  Basically, a firewall is a cybersecurity solution that protects your computer or network from unwanted traffic coming in or going out.

* #### Why is the traffic served over HTTPS
  HTTPS ensures that any data transferred between the visitor and the website cannot be tampered with or modified by a hacker.

* #### What monitoring is used for
  It is used to track changes in program performance over time.

* #### How the monitoring tool is collecting data
  collect data from the hardware that is supporting the virtual machines since hardware health knowledge is crucial to improving uptime.

* #### Explain what to do if you want to monitor your web server QPS
  There are dozens of web servers, but the two most popular are Apache and NGINX.
  * Request rate: The number of requests that the server receives over time. High request rates could indicate a recent increase in traffic.
  * Response time: The time to send a response to a request. High response times could indicate problems with the web server, host, or website resources, and result in frustrated users.
  * Response size: The amount of data delivered with each response (typically measured in bytes). Smaller responses use less network bandwidth and load faster for users, especially over limited and mobile connections.
  * Active connections: The number of requests currently being fulfilled. Too many active connections can exhaust the host’s available network ports, preventing new users from connecting.

## explain what the issues are with this infrastructure

* #### Why terminating SSL at the load balancer level is an issue
  Because of this, the customer's back-end nodes don't know what protocol the client requested.

* #### Why having only one MySQL server capable of accepting writes is an issue
  It assumes that you have a single master server that accepts reads and writes and one or more read-only slave servers. Data from the master server is replicated asynchronously to the slave servers.

* #### Why having servers with all the same components (database, web server and application server) might be a problem
  In some cases, even when power is restored, it takes some time for the server to reboot. If you haven’t already, look into implementing a backup power system, at least one capable enough to carry the supply of your server. This tool is especially important if your business is based in a location that experiences volatile weather conditions or unstable power supply.
