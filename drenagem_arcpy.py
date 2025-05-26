# -*- coding: utf-8 -*-
"""
Script: drenagem_arcpy.py
Descrição: Gera rede de drenagem a partir de um DEM usando ArcPy.
Autor: @bcandeia e @nathaliaolisil 
Como usar:
1. Ajuste o caminho da variável `wksp` para a pasta de trabalho.
2. Garanta que o Spatial Analyst esteja habilitado na licença.
3. Substitua 'outraster' (DEM) ou demais variáveis conforme necessário.
"""

# Importar módulos ArcPy
import arcpy
from arcpy import env
from arcpy.sa import *

# Verificar licença do Spatial Analyst
arcpy.CheckOutExtension("spatial")

# Definir workspace
wksp = env.workspace = r"C:\drenagem"  # <- Ajuste para o seu diretório

# Atribuir variáveis de entrada/saída
inFill                 = wksp + "\\fill"
in_flow_direction_raster = wksp + "\\fd"
in_conditional_raster  = wksp + "\\fa"
inStreamRaster         = wksp + "\\con_final"  # raster binário (1 = canal)
outStreamFeats         = wksp + "\\stream_final"  # shapefile de saída

# ------------------------------------------------------------------
# Passo 1: Fill
outFill = Fill(wksp + "\\grid", "")
outFill.save(inFill)

# Passo 2: Flow Direction
outFlowDirection = FlowDirection(inFill, "NORMAL", "")
outFlowDirection.save(in_flow_direction_raster)

# Passo 3: Flow Accumulation
outFlowAccumulation = FlowAccumulation(in_flow_direction_raster, "", "")
outFlowAccumulation.save(in_conditional_raster)

# Passo 4: Condicional (limiar > 150 células)
outCon = Con(in_conditional_raster, "1", "", "VALUE > 150")
outCon.save(inStreamRaster)

# Passo 5: Stream to Feature
StreamToFeature(
    inStreamRaster,
    in_flow_direction_raster,
    outStreamFeats,
    "NO_SIMPLIFY"
)

print("Processo concluído. Shapefile salvo em:", outStreamFeats)
