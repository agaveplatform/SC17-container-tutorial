# Getting Started with Agave
---

Agave is a multi-tenant [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer), and all interaction with it boils down to standard HTTP requests. There are actually tons of ways to generate those requests, depending on your preferences.  First things first,

## Tenants
The hosted Agave API has a number of different tenants.  A tenant is an isolated environment that can share core resources.  A tenant has its own isolated set of users, systems, apps, metadata, etc.  A tenant, depending on the configuration, can share some resources like backend workers in the cloud that drive the functionality of the service.  It's very much like an apartment complex that has independent spaces that share some underlying utilities, like power or water infrastructure.

For this tutorial, we are using the public Agave tenant.  There are multiple ways to access this, but you need an account first.  Go to:

http://public.agaveapi.co/create_account

Once you have an account, you can login different ways:

## Agave JupyterHub

The easiest way to get started is to use the hosted JupyterHub located at https://jupyter.agaveapi.co.  Login with the credentials you just created.

## Command line access

Agave has a great set of command-line utilities on bitbucket.  They only need bash and Python's JSON tool to work, which, if you are on a Linux or Mac system is probably already there.  Pull down the tools using git:

```
git clone https://bitbucket.org/agaveapi/cli.git
export PATH=$PATH:$PWD/cli
```

### Creating a client

The Agave API uses OAuth 2 for managing authentication and authorization. Before you start working with the API on the command line, you will need to create a OAuth client application associated with a set of API keys. This is a one-time action, so if you already have a set of API keys, skip to the next tutorial. If not, you can create your keys using the Clients service as follows:

```
clients-create -S -N my_client -D "Client used for app development"
```

Note: The -N flag allows you to specify a machine-readable name for your application; -D provides the description, and -S option stores your API keys for future use, so you will not need to manually enter them when you authenticate later.

After being prompted for your username and password, you should get a response letting you know if a client key and secret was generated successfully.  If you used the "-S" flag, as in the example, the CLI tools also cached that information in the ~/.agave/ directory.

Although much of the process of interacting with the Agave API is automated, you may need access to the consumerKey and consumerSecret for other types of OAuth2-based interaction so please record them. If you lose them, you can create new copy of them for the same client by deleting the old client and creating it again. You can also have multiple OAuth2 clients - we are simply demonstrating use of one.

### Obtaining an OAuth 2 authentication token

Tokens are a form of short-lived, temporary authenticiation and authorization used in place of your username and password. To interact with CyVerse APIs, you will need to acquire one. Your Cyverse token will expire 4 hours, but can easily be refreshed.

The command to accomplish this is:

```sh
# From your terminal interface, type:
auth-tokens-create -S
```
You will then be prompted to enter your *API password*.

### Refreshing your token

When your token expires in 4 hours, you may refresh it:

```sh
auth-tokens-refresh -S
```

This topic is covered in great detail at [Authorization Guide](http://agaveapi.co/documentation/authorization-guide/) in the Agave live docs
