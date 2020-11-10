@echo "cleaning up project"
mkdir './test/orant'
cp -r './test/orant_prev/* ./test/orant/'
rm -r './test/orant_prev'
rm '/test/destination/*.*'