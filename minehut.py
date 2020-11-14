import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Minehut.py v1.1.0
# Author: Razod (Mason Trv) <https://github.com/razod>
# License: MIT

class minehut():

    def __init__(self):
        pass

    def getServers(self):
        headers = {
            'content-type': 'application/json; charset=utf-8',
        }
        response = requests.get('https://api.minehut.com/servers', headers=headers ,verify=False)
        j = json.loads(response.content)
        return j
    
    def getServerByID(self, id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
        }
        response = requests.get('https://api.minehut.com/server/' + id, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def getServerByName(self, name):
        headers = {
            'content-type': 'application/json; charset=utf-8',
        }
        name = 'https://api.minehut.com/server/' + name + '?byName=true'
        response = requests.get(name, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def getPublicPlugins(self):
        headers = {
            'content-type': 'application/json; charset=utf-8',
        }
        response = requests.get('https://api.minehut.com/plugins_public', headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def userSignup(self, email):
        headers = {
            'content-type': 'application/json; charset=utf-8',
        }
        requestbody = {
            "email": email,
            "birthday": "1986-01-02T00:05:40.082Z",
        }
        response = requests.post('https://api.minehut.com/users/signup', headers=headers ,verify=False, json=requestbody)
        j = json.loads(response.content)
        return j

    def userConfirmEmail(self, code, password):
        headers = {
            'content-type': 'application/json; charset=utf-8',
        }
        requestbody = {
            "email_code": code,
            "password": password
        }
        response = requests.post('https://api.minehut.com/users/confirm_email', headers=headers ,verify=False, json=requestbody)
        j = json.loads(response.content)
        return j

    def userLogin(self, email, password):
        headers = {
            'content-type': 'application/json; charset=utf-8',
        }
        requestbody = {
            "email": email,
            "password": password,
        }
        response = requests.post('https://api.minehut.com/users/login', headers=headers ,verify=False, json=requestbody)
        j = json.loads(response.content)
        return j

    def ghostLogin(self, xsessionid):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
        }
        response = requests.post('https://api.minehut.com/users/ghost_login', headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def getUserByID(self, token, xsessionid, userid):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        name = 'https://api.minehut.com/user/' + userid
        response = requests.get(name, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def createServer(self, token, xsessionid, server_name):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "name": server_name,
            "platform": "java"
        }
        
        response = requests.post('https://api.minehut.com/servers/create', headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def getServerData(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/server_data"
        response = requests.get(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def getServerStatus(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/status"
        response = requests.get(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def hibernationServerStart(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/start_service"
        response = requests.post(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def startServer(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/start"
        response = requests.post(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def shutdownServer(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/shutdown"
        response = requests.post(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def immediatelyStopServer(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/destroy_service"
        response = requests.post(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def repairServerFiles(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/repair_files"
        response = requests.post(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def resetServer(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/reset_all"
        response = requests.post(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def sendCommandToServer(self, token, xsessionid, server_id, command):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "command": command
        }
        url = "https://api.minehut.com/server/" + server_id + "/send_command"
        response = requests.post(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def changeServerName(self, token, xsessionid, server_id, new_name):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "name": new_name
        }
        url = "https://api.minehut.com/server/" + server_id + "/change_name"
        response = requests.post(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def changeServerMOTD(self, token, xsessionid, server_id, new_motd):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "motd": new_motd
        }
        url = "https://api.minehut.com/server/" + server_id + "/change_motd"
        response = requests.post(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def changeServerVisibility(self, token, xsessionid, server_id, visibility):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "visibility": visibility
        }
        url = "https://api.minehut.com/server/" + server_id + "/visibility"
        response = requests.post(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def saveServer(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/save"
        response = requests.post(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def resetServerWorld(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/reset_world"
        response = requests.post(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def editServerProperties(self, token, xsessionid, server_id, field, value):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "field": field,
            "value": value,
        }
        url = "https://api.minehut.com/server/" + server_id + "/edit_server_properties"
        response = requests.post(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def getAllPlugins(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/server/" + server_id + "/plugins"
        response = requests.get(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j
    
    def installPlugin(self, token, xsessionid, server_id, plugin_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "plugin": plugin_id,
        }
        url = "https://api.minehut.com/server/" + server_id + "/install_plugin"
        response = requests.post(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def removePlugin(self, token, xsessionid, server_id, plugin_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "plugin": plugin_id,
        }
        url = "https://api.minehut.com/server/" + server_id + "/remove_plugin"
        response = requests.post(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def removePluginData(self, token, xsessionid, server_id, plugin_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "plugin": plugin_id,
        }
        url = "https://api.minehut.com/server/" + server_id + "/remove_plugin_data"
        response = requests.post(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def listRootFiles(self, token, xsessionid, server_id):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/file/" + server_id + "/list"
        response = requests.get(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def listFileDir(self, token, xsessionid, server_id, directory):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/file/" + server_id + "/list/" + directory
        response = requests.get(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def readFile(self, token, xsessionid, server_id, file_path):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/file/" + server_id + "/read/" + file_path
        response = requests.get(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j
        
    def editFile(self, token, xsessionid, server_id, file_path, content):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "content": content
        }
        url = "https://api.minehut.com/file/" + server_id + "/edit/" + file_path
        response = requests.get(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j

    def deleteFile(self, token, xsessionid, server_id, file_path):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        url = "https://api.minehut.com/file/" + server_id + "/delete/" + file_path
        response = requests.get(url, headers=headers ,verify=False)
        j = json.loads(response.content)
        return j

    def createFolder(self, token, xsessionid, server_id, path, name):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'x-session-id': xsessionid,
            'Authorization': token
        }
        reqbody = {
            "directory": path,
            "name": name
        }
        url = "https://api.minehut.com/file/" + server_id + "/folder/create"
        response = requests.get(url, headers=headers ,verify=False, json=reqbody)
        j = json.loads(response.content)
        return j