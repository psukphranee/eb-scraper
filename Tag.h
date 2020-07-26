#ifndef TAG_H
#define TAG_H

class Tag{

    public:

    explicit Tag(string name) : tagName(name){}
    string tagName;
    map<string, string> tagProperties;

    Tag *parentTag;
    Tag *childTag;
};


#endif
