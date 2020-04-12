from edtools import *

class Tree:
	
	def __init__( self ):

		self.tree = {}
		self.treeMap = ""
		self.selectorContainer = {}



	#------------------------------------------------------
	#	Getters
	#------------------------------------------------------

	def getTree( self ):
		return self.tree


	def getFullPath( self, tree = None, deleteTerms = None  ):

		result = {}

		def printLine( tree, subProcces=0, folderName = "" ):

			if getType(tree) == "dict":

				for key in tree:

					newList = tree[key]

					if getType( newList ) == "dict":


						fullPath = folderName + key + "/"

						# deleting terms by user, as rootDomain of a web Backup
						if getType( deleteTerms ) == "list":
							for term in deleteTerms:
								fullPath = fullPath.replace( term, "")

						# converting reults to relative
						fullPath = fullPath.replace("https://", "").replace("http://", "").replace("//", "/")

						# deleting first slash if exist
						if fullPath[:1] == "/":
							fullPath = fullPath[1:]

						result[ key ] = fullPath


						if len(newList):
							printLine( newList, subProcces + 1, folderName = fullPath )

					else:
						#print(folderName + key + ".ext")
						pass

			else:
				print(str(tree) + " is not a <dict> type ")


		if not tree:
			dataDict = self.tree
		else:
			dataDict = tree

		printLine( dataDict )


		return result









	# return 0 if not exist key,
	# if exist return de name and data
	def keyExist(self , name, tree = None ):


		def exist( dataDict, name, subProcces = 0):


			for key in dataDict:

				if key == name:

					resultDict = {
						"key":key,
					    "container":dataDict
					}

					self.selectorContainer = resultDict

					return resultDict

				else:
					newDict = dataDict[key]
					if len(newDict):
						result = exist(newDict, name, subProcces = subProcces + 1)
						if result:
							return result

			self.selector = {}
			self.selectorCopy = {}

			return 0


		#-------------------------------------------------

		if not tree:
			dataDict = self.tree
		else:
			dataDict = tree

		# if input is a <dict> type file
		if getType( dataDict ) == "dict":
			node = exist( dataDict, name )
			if node:
				return node

		return 0


	#------------------------------------------------------
	#	Setters
	#------------------------------------------------------

	def setTree( self, dictionary ):
		self.tree = dictionary
		return self


	#------------------------------------------------------
	#	ACTIONS
	#------------------------------------------------------

	def copy(self,src,dst):

		nodeSrc = self.keyExist( src )
		nodeDst = self.keyExist( dst )

		if nodeSrc and nodeDst:
			nodeSrc = nodeSrc["container"][ src ]
			nodeDst["container"][ dst ][ src ] = nodeSrc

		return self

	def move(self,src,dst):

		nodeSrc = self.keyExist( src )
		nodeDst = self.keyExist( dst )

		if nodeSrc and nodeDst:
			nodeSrcData = nodeSrc["container"][ src ]
			nodeDst["container"][ dst ][ src ] = nodeSrcData
			del nodeSrc["container"][ src ]

		return self

	def rename(self,src,dst):

		result = self.keyExist( src )

		if result:
			result["container"][ dst ] = result["container"][ src ]
			del result["container"][ src ]

		return self


	def delete(self,name):
		node = self.keyExist( name )
		if node:
			del node["container"][name]

		return self


	#------------------------------------------------------
	#	UTILS
	#------------------------------------------------------

	def printTree( self, tree = None ):

		self.treeMap = ""

		def printLine( tree, subProcces=0):


			if getType(tree) == "dict":

				for key in tree:

					newList = tree[key]

					key = key.replace("https://", "").replace("http://", "").replace("/", "")

					if getType( newList ) == "dict":
						self.treeMap += "|\t" * subProcces + key + "\n"
						print("|\t" * subProcces + key + "")

						if len(newList):
							printLine(newList, subProcces + 1)

					else:
						self.treeMap += "|\t" * subProcces + key + "\n"
						print("|\t" * subProcces + key + ".ext")

			else:
				print(str(tree) + " is not a <dict> type ")



		if not tree:
			dataDict = self.tree
		else:
			dataDict = tree

		print("\n\n\n")
		printLine( dataDict )
		print("\n\n\n")

		return "\n\n" + self.treeMap




	def getExampleTree( self ):

		tree = {"root": {
			"tiempo": {},
			"google": {
				"cuentas": {
					"free": {}
				}
			},
			"espectador": {
				"noticias": {},
				"deportes": {},
				"economia": {
					"interna": {},
					"externa": {
						"asia": {},
						"europa": {
							"folder": {
								"subfolder": {
									"file1": "",
									"file2": "",
									"file3": ""
								}
							},
							"file": ""
						}
					}
				}
			}
		}}

		return tree
