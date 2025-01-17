import os

import matplotlib.pyplot as plt
import pandas as pd

from src.cellData import cellData
from src.cellExtractOCV import cellExtractOCV
from src.cellTrainValidate import cellTrainValidate
from src.cellSimHyst import cellSimHyst
from src.plotData import plotData


def main():
    """

    Main function that calls desired functions
    
    Args:
        None
    Returns:
        None
    
    """
    # Create list of tests available from dataset
    pathname = (
        "datasets/lg-18650hg2/LG_HG2_Original_Dataset_McMasterUniversity_Jan_2020/"
    )

    # Define test temperature in deg C
    temp = "25degC/"

    # Obtain a list of filenames in above pathname
    filenames = [
        filename
        for filename in os.listdir(pathname + temp)
        if filename.endswith(".csv")
    ]

    # Create pandas dataframe with length of filenames as number of rows
    d = pd.DataFrame(filenames)

    # Convert dataframe to csv
    d.to_csv("filenames.csv", header=None, index=False)

    # Save dataframe as list of available tests done to csv
    filename = temp + "549_C20DisCh.csv"

    # Create class objects
    cellDataObj = cellData(filename, pathname)
    plotDataObj = plotData()

    cellDataObj.extractData()
    # plotDataObj.plotDataFromDataset(cellDataObj)

    # cellExtractOCVObj = cellExtractOCV(cellDataObj)
    # cellExtractOCVObj.runOCV()
    # plotDataObj.plotComputedOCV(cellExtractOCVObj)

    # train/validate model parameters
    # filename = temp + "551_Mixed1.csv"
    # filename = temp + "551_US06.csv"
    filename = temp + "551_LA92.csv"
    cellDataObj = cellData(filename, pathname)

    cellDataObj.extractData()
    # plotDataObj.plotDataFromDataset(cellDataObj)

    cellTrainValidateObj = cellTrainValidate(cellDataObj)
    # cellTrainValidateObj.runSimTrain()
    # cellTrainValidateObj.runSimValidate()
    cellTrainValidateObj.runCostVisualize()
    # plotDataObj.plotLoadedOCV(cellTrainValidateObj)
    # plotDataObj.plotDynamic(cellTrainValidateObj)
    plotDataObj.plotCostVisulaize(cellTrainValidateObj)

    # cellSimHystObj = cellSimHyst(cellDataObj)
    # cellSimHystObj.runSimTrain()
    # cellSimHystObj.runSimValidate()
    # plotDataObj.plotLoadedOCV(cellSimHystObj)
    # plotDataObj.plotDynamic(cellSimHystObj)

    plt.show()


if __name__ == "__main__":
    main()
