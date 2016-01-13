{
  'targets': [
    {
      'target_name': 'hiredis',
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
