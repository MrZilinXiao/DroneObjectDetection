#include <string.h>
#include <fstream>
#include <sstream>
#include <iostream>
#include <io.h>
#include <vector>
#include <stdlib.h>
using namespace std;

const string baseFilePath = "E:\\DataSet\\VisDrone2018-DET-train\\annotations1\\";
/************************************************************************/
/*  获取文件夹下所有文件名
输入：
path    :   文件夹路径
exd     :   所要获取的文件名后缀，如jpg、png等；如果希望获取所有
文件名, exd = ""
输出：
files   :   获取的文件名列表
*/
/************************************************************************/
void getFiles(string path, string exd, vector<string>& files)
{
	//文件句柄
	long   hFile = 0;
	//文件信息
	struct _finddata_t fileinfo;
	string pathName, exdName;

	if (0 != strcmp(exd.c_str(), ""))
	{
		exdName = "\\*." + exd;
	}
	else
	{
		exdName = "\\*";
	}

	if ((hFile = _findfirst(pathName.assign(path).append(exdName).c_str(), &fileinfo)) != -1)
	{
		do
		{
			//如果是文件夹中仍有文件夹,迭代之
			//如果不是,加入列表
			if ((fileinfo.attrib &  _A_SUBDIR))
			{
				if (strcmp(fileinfo.name, ".") != 0 && strcmp(fileinfo.name, "..") != 0)
					getFiles(pathName.assign(path).append("\\").append(fileinfo.name), exd, files);
			}
			else
			{
				if (strcmp(fileinfo.name, ".") != 0 && strcmp(fileinfo.name, "..") != 0)
					files.push_back(pathName.assign(/*path).append("\\").append(*/fileinfo.name));
			}
		} while (_findnext(hFile, &fileinfo) == 0);
		_findclose(hFile);
	}
}
int main(){
	vector <string> files;
	vector <string> totalStr;
	getFiles(baseFilePath, "txt", files);
	for (int i = 0; i < files.size(); i++){
		std::cout << files[i] << endl;
		ifstream inf;
		inf.open(baseFilePath+"\\"+files[i], ifstream::in);
		ofstream outf(baseFilePath+ "xml1\\" + files[i]);
		//outf.open("xml\\" + files[k], ifstream::out);

		const int cnt = 8;
		string line;
		string str = "";
		string clsStr = "";
		int j = 0;
		size_t comma = 0;
		size_t comma1 = 0;
		size_t comma2 = 0;

		while (!inf.eof()){
			comma1 = files[i].find('.', 0);
			totalStr.push_back(files[i].substr(0, comma1) + ".jpg");
			//outf << files[i].substr(0, comma1)+".jpg" << ' ';
			getline(inf, line);
			comma = line.find(',', 0);
			str =line.substr(0, comma);
			totalStr.push_back(str);
			//outf << str << ' ';
			while (comma < line.size() && j != cnt - 1){
				comma2 = line.find(',', comma + 1);
				str = line.substr(comma + 1, comma2 - comma - 1);
				totalStr.push_back(str);
				//outf << str << ' ';
				++j;
				comma = comma2;
			}
			//ignored regions (0), pedestrian (1), people (2), bicycle (3), car (4), van (5),
			//truck (6), tricycle (7), awning-tricycle (8), bus (9), motor (10), others (11))
			clsStr = "";
			switch (atoi(totalStr[6].c_str())){
			case 0:
				clsStr = "ignored regions";
				break;
			case 1:
				clsStr = "pedestrian";
				break;
			case 2:
				clsStr = "people";
				break;
			case 3:
				clsStr = "bicycle";
				break;
			case 4:
				clsStr = "car";
				break;
			case 5:
				clsStr = "van";
				break;
			case 6:
				clsStr = "truck";
				break;
			case 7:
				clsStr = "tricycle";
				break;
			case 8:
				clsStr = "awning-tricycle";
				break;
			case 9:
				clsStr = "bus";
				break;
			case 10:
				clsStr = "motor";
				break;
			case 11:
				clsStr = "others";
				break;
			}

			totalStr[6] = clsStr;

			//忽略第5个参数 score为0的
			if (totalStr[5] == "0"){
				totalStr.clear();
				j = 0;
			}
			else{
			    if (totalStr[6] == "ignored regions"||totalStr[6] == "pedestrian"||totalStr[6] == "people"||totalStr[6] == "bicycle"||totalStr[6] == "awning-tricycle"||totalStr[6] == "others")
                    cout<<"Ignoring this type!"<<endl; //忽略不需要的类别
                else
                    outf << totalStr[0] << ' ' << totalStr[6] << ' ' << totalStr[1] << ' ' << totalStr[2] << ' '
					<< to_string(atoi(totalStr[1].c_str()) + atoi(totalStr[3].c_str())) << ' '
					<< to_string(atoi(totalStr[2].c_str()) + atoi(totalStr[4].c_str())) << ' '
					<< totalStr[7] << endl;
				totalStr.clear();
				j = 0;
			}
		}
		inf.close();
		outf.close();
	}
	return 0;
}
