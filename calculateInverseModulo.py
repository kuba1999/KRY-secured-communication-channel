import gmpy

n = long("76896662714508286744734522772713649137443706128590068779597453717856379874574814984143284622510044159265596543879704128520614753614111118900605723370408179509385635026071171753753971595311787642734631255964171862122769944457180726400998943127699312803767434715288361724087668246765014517459204849384289109400945501970120079571242292263003580693943675421103055474447477714088715152187480821234096948376237000274125436883412941520149190410628950218970046258316526819969725037214674496182020171795914405397978564551277552586278109771686568007143134450111699204213342342246127354528257251352614071191397288071566525113181")

s = [
	long("74332719096221206106095413109489442556412674825434719873207141231851147737127197391906741598378504415959602075501335730289813436398489742995603068854079752404138620323703523041117245732819213883599503815599719939011116914832748780029602379931307630902807316035557622033926441147418919531413079746799717078336"),
	long("34872423687895948428383046966107511012117343192669254962765777779167265970438768720409291600764875802011258131118791825955444630625044507357502490713148628813640088619004105947852159225019387159440126413970642011808579287084591173223680469549109603755406534478566040384522623608286101341827824102274449010401"),
	long("154874163956744654818223171147503719881005243825222810855281925580645726002292528891363223824988118532934654806025539745793215266303695143314960370281470732554958348495153722762842459578689270168248409950672481662102930532316997181076101143593794661738568873661056606515862323851655244966058759536498402546110"),
	long("90761665601646844651874079550419223979545228246924857894861745496960497633116803179399235548823409620329490285982281551498256601593209568547304258261773115719927800553084059490714000470243912034525631436146559327997445304567545288585238956417308223117366103775979382748152531523918526831273669131563912108610"),
	long("70591149646013650282127363446502672482449011466152863456069689438100848192363965221299505245557948640825363164209577481601061253869431281202879732120328023727065207546957618097079507197453223657851919497522813135612253171142504691590575945034609152321017730419383304128475930585712721782107349425188100936001")
]	

k = 5

print "Pro b = 0"

for i in range(0, k):
	print "s_" + str(i) + ": " + str(gmpy.invert(long(pow(-1, 0))*long(pow(s[i],2)), n))
	print ""


print "Pro b = 1"

for i in range(0, k):
	print "s_" + str(i) + ": " + str(gmpy.invert(pow(-1, 1)*(pow(s[i],2)), n))
	print ""


