# 1-distributed_web_infrastructure
design a three server web infrastructure that hosts the website www.foobar.com.

![three server web infrastructure](https://res.cloudinary.com/elassari/image/upload/v1698525637/alx/kyxmbgdtnxviqr501q9e.png)

## Requirements
* 2 servers
* 1 web server (Nginx)
* 1 application server
* 1 load-balancer (HAproxy)
* 1 set of application files (your code base)
* 1 database (MySQL)

## specifics about this infrastructure
* ##### For every additional element, why you are adding it?
  To achieve the objective of reducing error rate on a consistent and transparent basis.

* ##### What distribution algorithm your load balancer is configured with and how it works
  Least Connection load balancing method

  ###### how it works 
  * Run application server maintenance or upgrades without application downtime
  * Provide automatic disaster recovery to backup sites
  * Perform health checks and prevent issues that can cause downtime

* ##### Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
  ###### Active/Active mode:
  is employed to provide for database or session replication and to support redundancy.
  ###### Active/Passive:
  configuration will offer you many advantages, so consider buying a pair of load balancers and configuring them in H/A mode. When this is done, the primary load balancer distributes the network traffic to the most suitable server

* ##### How a database Primary-Replica (Master-Slave) cluster works
  The master-slave is a database architecture divided into a master database and slave databases.
  ###### Slave database
  The slave database serves as the backup for the master database.
  ###### master database
  The master database is used for the write operations

* ##### What is the difference between the Primary node and the Replica node in regard to the application
  Each document in an index belongs to one primary shard. A replica shard is a copy of a primary shard

## The issues are with this infrastructure
* ##### Where are SPOF
  SPOFs are common in complex systems with interconnected components in multiple layers

* ##### Security issues (no firewall, no HTTPS)
  * Don’t provide complete protection against malicious websites and other online threats
  * Can be bypassed by hackers using techniques like port redirection or IP spoofing
  * Can create compatibility issues when switching vendors

* ##### No monitoring
  Vulnerability One of the biggest problems of not monitoring your network is vulnerability issues.
  Without proper network monitoring, your network could have vulnerabilities your organization may not know about that can lead to cyberattacks.
