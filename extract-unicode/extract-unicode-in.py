
languages = {  'devanagiri' : (0x0900, 0x097F),
                    'kannada' : (0x0c80, 0x0cff),
                    'telugu' : (0x0c00, 0x0c7f),
                    'tamil' : (0x0b80, 0x0bff),
                    'malayalam' : (0xd00, 0x0d7f)
                  }


exceptions = { 'devanagiri' : {},

               'kannada' : { 0x0c8d, 
                             0x0c91, 
                             0x0ca9, 
                             0x0cb4, 0x0cba, 0x0cbb, 
                             0xcc5, 0x0cc9, 0x0cce, 0x0ccf, 
                             (0x0cd0, 0x0cd4), (0x0cd7, 0x0cdc), 0x0cdf,
                             0x0ce4, 0x0ce5, 
                             0x0cf0, (0x0cf3, 0x0cff)
                },

               'telugu' : { 0x0c0d, 
                            0x0c11, 
                            0x0c29,
                            0x0c3a, 0x0c3b, 
                            0x0c45, 0x0c49, 0x0c4e, 0x0c4f,
                            (0x0c50, 0x0c54), 0x0c57, 0x0c5b, 0x0c5c, 0x0c5e, 0x0c5f,
                            0x0c4b, 0x0c4c, 
                            0x0c70, 0x0c76

                },

               'tamil' : { 0x0b80, 0x0b81, 0x0b84, (0x0b80b, 0x0b8d),
                           0x0b91, (0x0b96, 0x0b99), 0x0b9b, 0x0b9d,
                           (0x0ba0, 0x0ba2), (0x0ba5, 0x0ba7), (0x0bab,  0x0bad), 
                           (0x0bba, 0x0bbd), 
                           (0x0bc3, 0x0bc5), 0x0bc9, (0x0bce, 0x0bcf), 
                           (0x0bd1, 0x0bd6), (0x0bd8, 0x0bdf),  
                           (0x0be0, 0x0be5),   
                           (0x0bfb, 0x0bff) 
               },
               'malayalam' : { 0x0d0d,
                               0x0d11,
                               0x0d45, 0x0d49,
                               (0x0d50, 0x0d53),
                               0x0d64, 0x0d65     
                            }
             }


def valid_codes():
    for language in languages:
        
        expand_range = lambda x,y: { hex(i) for i in range( *(lambda x, y: (int(x), int(y)+1))(x,y) ) }

        lang_exceptions =  set()
        for code in exceptions[language]:
            if isinstance(code, tuple):
                lang_exceptions.update(expand_range(*code))
            else:
                lang_exceptions.add(hex(code))
                                    
      
        start, end = map(int, languages[language])
        for code in range(start, end+1):
            if hex(code) not in lang_exceptions:
                yield code






