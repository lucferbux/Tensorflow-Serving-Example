VENV=""
while getopts "he:" options; do
    case "${options}" in
        h)
            echo -e "Usage: $0 [ -h ] [ -e y/n ]\n" 1>&2
            echo -e "-e <y|n>\tSpecify if you want to enable virtualenv" 1>&2
            echo -e "-h\tShows this help\n" 1>&2
            exit 0
        ;;
        e)
            VENV=$(echo ${OPTARG} | tr '[:upper:]' '[:lower:]')
        ;;
    esac
done



if [ "$VENV" == "" ]; then
    read  -p "Do you want to create a virtual environment? (y/n): " VENV
fi

if [ "$VENV" == "y" ]
then
    pip3 install virtualenv
    virtualenv venv
    source venv/bin/activate
fi
echo "Installing python libraries..."
# Install Python dependencies
pip3 install --no-cache-dir -r ./requirements.txt
pip3 install --no-cache-dir -r ./modules/_requirements.txt

echo "Done!"

if [ "$VENV" == "y" ]
then
    echo "To activate virtualenv use: source venv/bin/activate"
    echo "To exit: deactivate"
fi