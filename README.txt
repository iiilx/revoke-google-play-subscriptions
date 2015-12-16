(Only an administrator on your Google Play account can perform the required steps)

Go to https://play.google.com/apps/publish/
Click the settings icon on left sidebar
Click API Access on left
Click Create Service Account towards bottom
Follow "step 1" to Navigate to Google Developer’s Console (opens a new tab).
Click "add credentials" (blue button)
Have the JSON radio button selected and click "Create"--a file will be downloaded to your computer.
Go back to the 1st tab and click Done.
Grant all permissions for this user
in the downloaded json file, `client_email` and `private_key` should be used in the revoke.py script
