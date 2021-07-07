package split

type TestCase struct {
	target string
	delimiterList []string
	isPrintDelimiter bool
}
func ExampleTest() {

	testCase := []TestCase{
		TestCase{">helloworld", []string{"|", " ", ">", "<"}, true},
		TestCase{"hello>wo|rld", []string{"|", " ", ">", "<"}, true},
		TestCase{"hello>>world", []string{"|", " ", ">", "<"}, true},
		TestCase{"hello>worl>>>dd", []string{">", ">>>", ">>"}, true},
		TestCase{"helloworld>>>>", []string{">", "<"}, true},
		TestCase{"helloworld>>>>", []string{">>", "><", ">"}, true},
		TestCase{"helloworld>>>>", []string{">>"}, true},
		TestCase{"helloworld>><>>", []string{"><", ">", ">>"}, true},
		TestCase{"helloworld>>>>>>>", []string{">>>", ">"}, true},
		TestCase{"ls -al /dev | grep example >>log.txt &", []string{">", ">>", "<", "<<", "|", "&", " "}, true},
		TestCase{"hello world", []string{" "}, false},
	}

	for _, test := range testCase {
		printSplitedArray(split(test.target, test.delimiterList, test.isPrintDelimiter))
	}

	// Output:
	// >:helloworld:
	// hello:>:wo:|:rld:
	// hello:>:>:world:
	// hello:>:worl:>>>:dd:
	// helloworld:>:>:>:>:
	// helloworld:>>:>>:
	// helloworld:>>:>>:
	// helloworld:>>:<:>>:
	// helloworld:>>>:>>>:>:
	// ls: :-al: :/dev: :|: :grep: :example: :>>:log.txt: :&:
	// hello:world:
}