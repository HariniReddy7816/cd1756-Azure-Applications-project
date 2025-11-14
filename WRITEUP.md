Resource Justification
Analysis of VM vs App Service
To determine the appropriate Azure resource for deploying the Article CMS application, I analyzed both Azure Virtual Machines (VMs) and Azure App Service using the required criteria: cost, scalability, availability, and workflow.
1. Cost
VM:
A VM typically costs more because I am paying for the full compute instance regardless of traffic. I am also responsible for OS updates, security patches, and storage. However, a VM can become cost-effective if I need full control of the environment or plan to host multiple components on the same machine.
App Service:
App Service is generally cheaper due to shared plans and automatic resource optimization. Costs scale based on usage, and Microsoft handles patching and maintenance. But App Service may require a higher tier if the application needs custom configurations.
2. Scalability
VM:
VMs scale manually or through Virtual Machine Scale Sets. Scaling is slower because entire VM instances need to start or stop. However, scaling on a VM gives full control over how the system behaves and supports custom background services.
App Service:
App Service has quick, one-click vertical and horizontal scaling. Autoscaling is built in and automatic. This makes scaling easier, especially for web apps with unpredictable workloads.
3. Availability
VM:
For VMs, I must configure availability sets or availability zones myself. The responsibility for patching, uptime, system monitoring, and OS security lies entirely with the developer. Even though it requires more work, a VM provides complete control over how the system behaves and how availability is maintained.
App Service:
App Service offers built-in high availability with automated patching, load balancing, and platform maintenance. Availability is easier to set up, but the developer has less control over the underlying environment.
4. Workflow
VM:
Deploying to a VM allows full control over the operating system, installed software, runtime versions, and security configurations. This is beneficial when the application needs a custom environment. The deployment workflow can be more complex because it requires managing the OS, installing packages, and configuring web servers manually.
App Service:
App Service provides simpler deployments using GitHub Actions, ZIP Deploy, or Docker. No OS configuration is needed, but the environment is more restrictive.
Chosen Resource & Justification
I chose to deploy the Article CMS using an Azure Virtual Machine (VM).
I selected a VM because it provides complete control over the environment, including the OS, installed packages, runtime versions, and server configuration. This flexibility is valuable for applications where I may need to modify system settings, install additional tools, or run background tasks that App Service does not support. A VM also allows me to manage the database connection, authentication configurations, and logging at the system level, which aligns well with the CMS requirements. Even though it involves more management overhead compared to App Service, the expanded control justifies using a VM for this deployment.
