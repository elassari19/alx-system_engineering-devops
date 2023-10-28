# simple web infrastructure
  A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

![simple web stack](https://res.cloudinary.com/elassari/image/upload/v1698525294/alx/ma4sqjl0ofaigtabvaov.png)

## Description
  On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via www.foobar.com. Start your explanation by having a user wanting to access your website.

## Requirements
  1 server
  1 web server (Nginx)
  1 application server
  1 application files (your code base)
  1 database (MySQL)
  1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

## About This Infrastructure
  * #### What is a server
      A server computer is a device or software that runs services to meet the needs of other computers

  * #### The role of the domain name
      A domain name is the unique name that each website has. Your domain is the place people need to go to visit your website, and each domain is completely unique.

  * #### The type of DNS record www is in www.foobar.com
      The record can be checked by running dig www.foobar.com. The www.foobar.com known as a DNS host record, stores a hostname

  * #### The role of the web server
      Verify that the required protocol
      Verify that the required hostname
      Verify that the TCP port used
      Verify that the path points to a physical file
      Handle the request and transmit the response

  * #### The role of the application server
      the application server is responsible for:
      * security
      * processing and serving files
      * processing and compiling files
      * serving the entire response generated back to the browser

  * #### The role of the database
      * Interpretation and presentation of data
      * Distribution of data and information
      * Data preservation and monitoring the data
      * Control over data duplication and use

  * #### What is the server using to communicate with the computer of the user requesting the website
      The communication between the client and the server through HTTP/HTTPS protocol

## what the issues are with this infrastructure:
  * #### SPOF (Single Point Of Failure) 
      A single point of failure is a part of a system that, if it fails, takes down the entire rest of the system too
  
  * #### Downtime when maintenance needed (like deploying new code web server needs to be restarted)
    Administrators should take preventative measures to ensure that a server experiences as little downtime as possible. Here are some best practices to help reduce downtime

  * #### Cannot scale if there's too much incoming traffic
    When server requests exceed available resources, performance suffers and eventually the server crashes. Cloud servers can expand resources dynamically, but on-premise administrators responsible for those cloud servers must always ensure that servers can support customer applications and resource expansions.
