import SigProfilerAssignment as spa
from SigProfilerAssignment import Analyzer as Analyze
for i in ["MKPV_4pic_sample", "smallpox4samples"]:
	samples     = "./"+i+".txt"
	output      = "./"+i+"/"

	sigs        = "/Dell/Dell15/zhangsy/humanTCGN/cosmic/COSMIC_v3.3.1_SBS_GRCh38.txt" #参考SBS特征

	#Analysis of SP Assignment 
	Analyze.cosmic_fit( samples, 
                    output, 
                    signatures=None,
                    signature_database=None,
                    genome_build="GRCh37",
                    cosmic_version=3.3,
                    verbose=False,
                    collapse_to_SBS96=False,
                    make_plots=True,
                    exclude_signature_subgroups=None,
                        exome=False)