#programa 1 hmmfilter - alinhamentos

import os
import glob
import sys
import subprocess


argumentos = sys.argv
total_arg = len(argumentos)

for i in range(total_arg):
	if sys.argv[i] == "-i":
		entrada = sys.argv[i+1]

#parametros hmmfilter********************************************************************************************************

p1_hmmfilter="0.80"
p2_hmmfilter="0.70"

print "lendo diretorio "+entrada
arquivos=glob.glob(entrada+"/*")

for arquivo in arquivos:

	nome_arquivo = arquivo.split("/")

	print "lendo arquivo "+ arquivo

	subprocess.call(["app/hmmfilter", arquivo, "output/saida_1/"+nome_arquivo[1]+"_out_",p1_hmmfilter, p2_hmmfilter])


#programa 2 getrefseq sequencia de referencia******************************************************************************************************** 

entrada=sys.argv[1]

#parametros getrefseq
p2="3"
p3="0"

print "lendo diretorio "+entrada
arquivos=glob.glob(entrada+"/*")

for arquivo in arquivos:

	nome_arquivo = arquivo.split("/")

	print "lendo arquivo "+ arquivo

	subprocess.call(["python","getRefSeqs.py",arquivo,p2,p3,"saida_getrefseq/"+nome_arquivo[1]+"_out_"])


#programa 3 conservedresidues********************************************************************************************************

entrada=sys.argv[1] # base_pfam
entrada1=sys.argv[2] # pasta saida_getrefseq

#parametros  conservedresidues
p4="0.8"


print "lendo diretorio "+entrada
arquivos=glob.glob(entrada+"/*")

for arquivo in arquivos:

	nome_arquivo = arquivo.split("/")

	print "lendo arquivo "+ arquivo


print "lendo diretorio "+entrada1
arquivos1=glob.glob(entrada1+"/*")

for arquivo1 in arquivos1:

	nome_arquivo1 = arquivo1.split("/")

	print "lendo arquivo "+ arquivo1
	subprocess.call(["./conservedresidues",arquivo,arquivo1,"saida_2/"+nome_arquivo1[1],p4])


