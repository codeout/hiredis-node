{
  'targets': [
    {
      'target_name': 'hiredis',
      'sources': [
          'src/hiredis.cc'
        , 'src/reader.cc'
      ],
      'include_dirs': ["<!(node -e \"require('nan')\")"],
      'defines': [
          '_GNU_SOURCE'
      ],
      'cflags': [
          '-Wall',
          '-O3'
      ]
    }
  ]
}
