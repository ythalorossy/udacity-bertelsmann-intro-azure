class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    # TODO: Enter your client secret from Azure AD below
    CLIENT_SECRET = "g-bLG5_qNb157_Uf.5KmZAdQl69vPnGHD." 

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    # Enter your application client ID here
    CLIENT_ID = "a954e328-04a3-46e8-8c20-e38ca79cc304"

    # Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session