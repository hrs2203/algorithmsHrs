# Title: Multilayer Architecture Model for Mobile CloudComputing Paradigm

## Objective of the work
The main objective of this work consists of researching architecture models that are able to increase the resilience and flexibility of off-loading the workload outside the device and to enable scheduling the tasks along the network.

A computational model of a multilayer architecture for increasing the performance of devices using the Mobile Cloud Computing paradigm. The main novelty of this work lies in defining a comprehensive model where all the available computing platforms along the network layers are involved to perform the outsourcing of the application workload. This proposal provides a generalization of the Mobile Cloud Computing paradigm which allows handling the complexity of scheduling tasks in such complex scenarios.

## Major contributions
The key contributions of this work can be summarized as follows.

(i) A study of the complexity and key issues of distributing the processing load among several computing layers along the network and a review of the architectures and network layers to perform this offloading process.

(ii) The proposal of a general framework for a multilayer architecture to formalize the processing of an application and the implications of the distributed configurations to the performance and the communications requirements.


## Approach Referred
Outsourcing Options for MCC. These outsourcing options are deployed at different layers of the network forming a pool of computing platforms thatare available depending on the application context.

a) In the top, at the network core, thecloud layerremainsthe most powerful computing platform.

b) Next, the cloudlet layer,  This infrastruc-ture is a “little” data center with the objective of bringingthe cloud closer to the users.
The main advantages provided by cloudlets are two fold:

1. to reduce service disruptions and delays caused by thenetwork to remote servers.
2. to ensure a high levelof security of the data since it does not need to be sent through Internet.

cloud lets are computing platforms similar to cloud servers but prepared and scaled accordingto the specific requirements of the organization.

c) Next, the same principle of cloudlets is applied to the MobileEdge Computing (MEC) Layer. A MEC server is a data centerin a box, that, in this case, it is deployed by the mobile telecom operators in close proximity to mobile subscribers.

d) Finally, The fog layer is a set of devices such as routers, switches, or other networking devices closer or within the end users' local networks.

<b>Proposed Distributed Architecture</b>: This approach attempts to identify methods to obtain the best computational results and performance using the network infrastructure deployments and local processing capabilities.

As a rule, it is advisable to perform the processing as close as possible to where the data are acquired to reduce the delay and global network traffic. the final decision on where to offload each task dependson many other aspects including application requirements,devices configuration, user preferences, size of input data,and pricing. 

Following are the technical characteristics of the MCC paradigm explained and how the proposed model utilizes them.

1. <b>The application partitioning method </b> is a critical aspect for enabling the outsourcing of the code at multiple heterogeneous layers of the network architecture.

2. <b>The offloading decision mechanism</b> the mechanism must calculate, for each layer, the offloading decision according to an optimization problem that addresses all the issues specified. This algorithm must be able to be executed quicklyto leverage the potential of the available resources.

3. <b>The offloading mode</b> for the proposed MCC architecture must meet the following minimum requirements: the method must be suitable for heterogeneous infrastructures and must use a light weight method so as to not overload the limited resources of the edge layers.

4. <b>The context-awareness feature</b> is important to perform offloading to several layers of the network. The desirable configuration requires a self-adaptive architecture to know what layers and devices are available at any time for offloading the work. It is significant to perform this feature without intervention of an administrator to shape dynamic environments.

5. <b>the cost-benefit function </b> must be computed oneach level of the architecture to determine where to perform the computation.

> Add Maths if needed, part 3.2 general concepts

## Experimental Details
The example application consists of an Augmented Reality (AR) system for Smart Cities which enables the user tomove freely through the modelled environment of the cityusing their mobile devices. 

This experiment describes how the proposed multilayer computational model can handle real-world scenarios in order to find the best execution cost for computing an application taking into account the different available offloading layers. For this purpose, three application contexts have been defined to test the model under different conditions.

1. <b>Battery Saving Application Context</b>: The general definition of these contexts is that the user device is configured tosave battery power. Battery consumption is a performanceaspect for only battery-powered devices such as mobiledevices or wireless sensors. Thus, it only applies to IoT devices.

2. <b>Monetary Cost Saving Application Context</b>: The general definition of this context is that the user device does not have performance enough to run the VR application. It is only used for displaying the results and, therefore, it has to outsource the processing load. In such a context, it is configured to save processing expenses when using an external computing platform.

3. <b>Real-Time Application Context</b>: The general definition of these contexts is to minimize the computing delay of the application in order to meet quality constraints of demanding real-time AR algorithms.

## Performance measuring metrics



## Outcome



## Limitations of the work.


