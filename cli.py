import argparse

def argparser() -> argparse.ArgumentParser:
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='bioseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action="store_true",
                             help="Convet DNA to reverse-complementary")
    
    enzTargetsScan_command = subparsers.add_parser('enzTargetsScan', help='finding restric enz. target site')
    enzTargetsScan_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enzTargetsScan_command.add_argument("-e", "--enz", type=str, default=None,
                             help="Enzyme name")  
    enzTargetsScan_command.add_argument("-r", "--revcomp", action="store_true",
                             help="Convet DNA to reverse-complementary")
    
    transcription_command = subparsers.add_parser('transcription', help='Convert DNA to RNA')
    transcription_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    transcription_command.add_argument("-r", "--revcomp", action="store_true",
                             help="Convet DNA to reverse-complementary")
    
    translation_command = subparsers.add_parser('translation', help='Translate DNA to Protein')
    translation_command.add_argument("-s", "--seq", type=str, default=None, 
                             help="Provide sequence")       
    translation_command.add_argument("-r", "--revcomp", action="store_true",
                             help="Convet DNA to reverse-complementary")
    
    cgcserch_command = subparsers.add_parser('cpgScan', help='Search for CpG sequence')
    cgcserch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    return parser

def main(argv=['-h']):

    print("Test:", " ".join(argv),"\n")
    parser = argparser()
    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        # Help (or parse error) triggered an exit; don't kill the process in this test.
        # argparse has already printed the help/usage text.
        print("============================\n")



if __name__ == "__main__":
    main(['-h'])
    main(['gcContent','-h'])
    main(['countBases','-h'])
    main(['enzTargetsScan','-h'])
    main(['transcription','-h'])
    main(['translation','-h'])
    main(['cpgScan','-h'])

